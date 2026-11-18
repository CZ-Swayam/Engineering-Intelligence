#!/usr/bin/env python3
"""Validate Engineering Intelligence repository content and metadata."""

from pathlib import Path
import json
import re
import sys

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "metadata" / "schemas"
TAXONOMIES_DIR = ROOT / "metadata" / "taxonomies"
ERRORS = []


def load_yaml(path):
    with path.open("r", encoding="utf-8") as stream:
        return yaml.safe_load(stream)


def load_schema(name):
    with (SCHEMAS / name).open("r", encoding="utf-8") as stream:
        return json.load(stream)


def validate_schema(data, schema, path):
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for error in validator.iter_errors(data):
        location = ".".join(str(part) for part in error.absolute_path) or "<root>"
        ERRORS.append(f"{path.relative_to(ROOT)}: {location}: {error.message}")


def load_taxonomies():
    result = {}
    for path in TAXONOMIES_DIR.glob("*.yaml"):
        data = load_yaml(path) or {}
        result[path.stem] = {
            item["id"] for item in data.get("values", [])
            if isinstance(item, dict) and "id" in item
        }
    return result


def check_values(path, label, values, allowed):
    for value in values:
        if value not in allowed:
            ERRORS.append(
                f"{path.relative_to(ROOT)}: unknown {label} value '{value}'"
            )


def read_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", text, re.DOTALL)
    if not match:
        ERRORS.append(f"{path.relative_to(ROOT)}: missing or malformed YAML frontmatter")
        return None
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        ERRORS.append(f"{path.relative_to(ROOT)}: invalid YAML frontmatter: {exc}")
        return None
    if not isinstance(data, dict):
        ERRORS.append(f"{path.relative_to(ROOT)}: frontmatter must be a YAML object")
        return None
    return data


def main():
    tax = load_taxonomies()
    knowledge_schema = load_schema("knowledge.schema.json")
    component_schema = load_schema("component.schema.json")
    implementation_schema = load_schema("implementation.schema.json")

    # Validate knowledge metadata.
    knowledge_records = []
    for path in sorted((ROOT / "knowledge").rglob("*.md")):
        if path.name.lower() == "readme.md":
            continue
        data = read_frontmatter(path)
        if data is None:
            continue
        knowledge_records.append((path, data))
        validate_schema(data, knowledge_schema, path)
        check_values(path, "category/domain", [data.get("category", "")], tax.get("domains", set()))
        check_values(path, "layer", data.get("layers", []), tax.get("layers", set()))
        check_values(path, "pattern", data.get("patterns", []), tax.get("patterns", set()))
        known_technologies = (
            tax.get("frameworks", set())
            | tax.get("databases", set())
            | tax.get("languages", set())
        )
        check_values(path, "technology", data.get("technologies", []), known_technologies)

    # Validate components and their implementation manifests.
    component_ids = set()
    for path in sorted((ROOT / "components").rglob("component.yaml")):
        try:
            component = load_yaml(path)
        except yaml.YAMLError as exc:
            ERRORS.append(f"{path.relative_to(ROOT)}: invalid YAML: {exc}")
            continue
        if not isinstance(component, dict):
            ERRORS.append(f"{path.relative_to(ROOT)}: component manifest must be a YAML object")
            continue

        validate_schema(component, component_schema, path)
        component_id = component.get("id")
        if component_id in component_ids:
            ERRORS.append(f"{path.relative_to(ROOT)}: duplicate component id '{component_id}'")
        if component_id:
            component_ids.add(component_id)

        check_values(path, "domain", [component.get("domain", "")], tax.get("domains", set()))
        check_values(path, "layer", component.get("layers", []), tax.get("layers", set()))
        check_values(path, "pattern", component.get("patterns", []), tax.get("patterns", set()))
        check_values(path, "capability", component.get("capabilities", []), tax.get("capabilities", set()))
        check_values(path, "database", component.get("databases", []), tax.get("databases", set()))

        for implementation in component.get("implementations", []):
            check_values(path, "language", [implementation.get("language", "")], tax.get("languages", set()))
            check_values(path, "framework", [implementation.get("framework", "")], tax.get("frameworks", set()))
            check_values(path, "distribution", implementation.get("distribution", []), tax.get("distribution-methods", set()))

            component_root = path.parent.resolve()
            implementation_dir = (component_root / implementation.get("path", "")).resolve()
            manifest_path = (component_root / implementation.get("manifest", "")).resolve()

            if not implementation_dir.is_relative_to(component_root):
                ERRORS.append(f"{path.relative_to(ROOT)}: implementation path escapes component directory")
                continue
            if not implementation_dir.is_dir():
                ERRORS.append(f"{path.relative_to(ROOT)}: missing implementation directory {implementation.get('path')}")
                continue
            if not manifest_path.is_relative_to(component_root) or not manifest_path.is_file():
                ERRORS.append(f"{path.relative_to(ROOT)}: missing or unsafe implementation manifest {implementation.get('manifest')}")
                continue

            try:
                implementation_data = load_yaml(manifest_path)
            except yaml.YAMLError as exc:
                ERRORS.append(f"{manifest_path.relative_to(ROOT)}: invalid YAML: {exc}")
                continue
            if not isinstance(implementation_data, dict):
                ERRORS.append(f"{manifest_path.relative_to(ROOT)}: implementation manifest must be a YAML object")
                continue

            validate_schema(implementation_data, implementation_schema, manifest_path)
            if implementation_data.get("id") != implementation.get("id"):
                ERRORS.append(f"{manifest_path.relative_to(ROOT)}: implementation id differs from component manifest")
            check_values(manifest_path, "language", [implementation_data.get("language", "")], tax.get("languages", set()))
            check_values(manifest_path, "framework", [implementation_data.get("framework", "")], tax.get("frameworks", set()))
            check_values(manifest_path, "capability", implementation_data.get("supported_capabilities", []), tax.get("capabilities", set()))
            check_values(manifest_path, "database", implementation_data.get("databases", []), tax.get("databases", set()))
            check_values(manifest_path, "distribution", implementation_data.get("distribution", []), tax.get("distribution-methods", set()))

            for directory in ("src", "tests", "examples"):
                if not (implementation_dir / directory).is_dir():
                    ERRORS.append(f"{implementation_dir.relative_to(ROOT)}: missing required directory '{directory}/'")

    # Validate knowledge-to-component references.
    for path, data in knowledge_records:
        for component_ref in data.get("related_components", []):
            if component_ref not in component_ids:
                ERRORS.append(f"{path.relative_to(ROOT)}: unknown related component '{component_ref}'")

    if ERRORS:
        print(f"Validation failed with {len(ERRORS)} error(s):")
        for error in ERRORS:
            print(f"- {error}")
        return 1

    print("Engineering Intelligence data repository validation passed.")
    print(f"Knowledge documents: {len(knowledge_records)}")
    print(f"Components: {len(component_ids)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
