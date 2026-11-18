# Contributing

## General

1. Prefer reusable engineering knowledge over one-off tutorials.
2. Use stable, lowercase, dot-separated IDs, such as `database.keyset-pagination`.
3. Use taxonomy identifiers exactly as defined in `metadata/taxonomies/`.
4. Keep logical component metadata separate from implementation metadata.
5. Give each implementation its own Semantic Version.
6. Add tests and examples when implementation behavior changes.
7. Run the repository validator before opening a pull request.

## Knowledge documents

Knowledge documents are Markdown files with YAML frontmatter. The contract is defined in `metadata/schemas/knowledge.schema.json`.

Suggested body sections:
- Problem and context
- Explanation
- When to use
- When not to use
- Trade-offs
- Implementation considerations
- References

Use authoritative references. Do not reproduce external standards or documentation.

## Components

A logical component directory contains:
- `component.yaml`
- `README.md`
- One or more implementation directories.

Each implementation directory contains:
- `manifest.yaml`
- `src/`
- `tests/`
- `examples/`

The logical component describes the capability. Each implementation manifest describes a particular language/framework realization.

## Taxonomy changes

Taxonomies are controlled vocabularies. Add new values through a pull request and include a concise description. Avoid synonyms and spelling variants for the same concept.
