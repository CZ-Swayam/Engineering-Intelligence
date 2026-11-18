# Engineering Intelligence

The canonical, Git-backed content repository for Engineering Intelligence.

This repository contains engineering knowledge, reusable components, organizational conventions, metadata contracts and controlled taxonomies. It does **not** contain the MCP server implementation or an agent client.

## Repository boundaries

| Repository | Responsibility |
|---|---|
| `engineering-intelligence` (this repository) | Knowledge, components, schemas, taxonomies and content governance |
| `engineering-intelligence-mcp` | Python MCP server, indexing, discovery and retrieval |
| `engineering-intelligence-client` (future) | Optional CLI, agent setup and integration workflows |

## Structure

```text
engineering-intelligence/
├── knowledge/
├── components/
├── organizational-standards/
├── metadata/
│   ├── schemas/
│   └── taxonomies/
├── releases/
├── scripts/
├── docs/
├── .github/
├── CONTRIBUTING.md
└── README.md
```

## Content principles

- GitHub is the canonical source of truth.
- Knowledge documents use Markdown with YAML frontmatter.
- Components represent logical engineering capabilities and may contain multiple language/framework implementations.
- Each implementation is independently versioned.
- Metadata values use controlled taxonomy identifiers.
- Organizational standards contain organization- or project-specific conventions only.
- Do not copy external industry standards or framework documentation into this repository. Link to authoritative sources; the consuming agent retrieves current guidance.
- Component source code is retrieved on demand by consumers. Metadata discovery should not require loading all source files.

## Validate this repository

The validator is a repository-maintenance script, not an installable Python package.

Requirements: Python 3.10+.

```bash
python -m pip install -r scripts/requirements.txt
python scripts/validate_repository.py
```

GitHub Actions runs the same validation on pushes and pull requests.

## Current contents

The starter includes:
- Version 1 metadata schemas and taxonomies.
- A starter LLD knowledge collection covering foundational principles and common design patterns.
- A keyset-pagination knowledge document.
- A logical pagination component with Django REST Framework and Spring Boot reference implementations.
- Repository validation and CI.

The examples are starter references, not certified production packages. Review and test them against your target frameworks and databases before adoption.
