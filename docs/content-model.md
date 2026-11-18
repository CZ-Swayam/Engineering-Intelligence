# Content model

## Knowledge documents

Markdown documents with YAML frontmatter. The metadata contract is `metadata/schemas/knowledge.schema.json`.

## Logical components

A component describes an engineering capability and lists one or more implementation variants. Its manifest is `component.yaml`.

## Implementations

Each implementation targets a language/framework combination and has its own `manifest.yaml`, source, tests and examples. Versions are independent and use Semantic Versioning.

## Taxonomies

Taxonomies provide canonical identifiers for domains, layers, languages, frameworks, databases, patterns, capabilities, distribution methods and maturity.

## Consumer contract

Consumers should:
1. Read schemas and taxonomies.
2. Parse manifests and knowledge frontmatter.
3. Build a metadata catalog from metadata only.
4. Filter and rank candidates.
5. Retrieve selected source files only when requested.

The data repository does not prescribe a database, search engine, MCP SDK or programming language for consumers.
