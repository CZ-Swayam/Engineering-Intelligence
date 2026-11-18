# Expected contract

- Negative page numbers are rejected.
- Requested page size is bounded to 1–200.
- Ordering is deterministic: `createdAt`, then `id`.

Add JUnit and repository integration tests in the consuming Spring Boot project.
