---
id: design-patterns.repository-pattern
title: Repository Pattern
category: architecture
tags:
- design-patterns
- data-access
- persistence
- domain-model
technologies: []
layers:
- domain
- application
- infrastructure
patterns:
- repository
summary: The Repository pattern provides a collection-like abstraction for retrieving
  and persisting domain objects while isolating data-access details.
related_components: []
references: []
last_reviewed: '2026-11-18'
status: published
---

# Repository Pattern

## Intent

Provide a boundary between domain/application logic and persistence details. A repository exposes operations in terms of the model or aggregate the application works with.

## Example

```text
OrderRepository
  findById(orderId)
  save(order)
  findPendingBefore(timestamp)
```

An infrastructure implementation may use SQL, an ORM or another storage system. The application service depends on the repository contract where that abstraction is useful.

## Benefits

- Isolates persistence technology and query mechanics.
- Makes application logic easier to test.
- Gives domain-oriented names to important queries.
- Can centralize aggregate persistence behavior.

## When it may be unnecessary

Many frameworks already provide effective repository abstractions. Adding another generic wrapper around every ORM method can create indirection without isolating meaningful complexity.

## Design guidance

- Model methods around use cases and domain concepts.
- Avoid exposing ORM-specific query objects through a domain-facing contract unless the architecture intentionally accepts that coupling.
- Be clear about transaction boundaries and unit-of-work behavior.
- Avoid returning partially loaded objects with surprising lazy-loading behavior.
- Do not make one generic repository responsible for unrelated aggregates.
