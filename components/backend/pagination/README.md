# Pagination component

This logical component groups implementations by engineering capability rather than treating each language/framework implementation as an unrelated component.

| Implementation | Language | Framework | Version |
|---|---|---|---|
| `django-rest-framework` | Python | Django REST Framework | 0.1.0 |
| `spring-boot` | Java | Spring Boot | 0.1.0 |

## Selection guidance

- Use page-number/offset pagination when arbitrary page navigation is required and data volumes are manageable.
- Consider keyset pagination for large datasets and sequential navigation with deterministic indexed sort keys.
- Validate database-specific behavior before adoption.

Each implementation is independently versioned. These are source-integration references, not published packages.
