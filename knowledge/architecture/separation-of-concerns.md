---
id: architecture.separation-of-concerns
title: Separation of Concerns
category: architecture
tags:
- separation-of-concerns
- layering
- modularity
technologies: []
layers:
- presentation
- application
- domain
- infrastructure
- cross-cutting
patterns: []
summary: Separation of concerns assigns distinct kinds of responsibility to clear
  modules or layers so changes remain localized and behavior is easier to reason about.
related_components: []
references: []
last_reviewed: '2026-11-18'
status: published
---

# Separation of Concerns

## Definition

A concern is a distinct responsibility or aspect of system behavior. Separation of concerns organizes code so that each part handles a coherent concern and communicates through explicit boundaries.

Typical concerns include:
- Transport and request parsing.
- Application workflow orchestration.
- Domain rules and invariants.
- Persistence.
- External service integration.
- Authentication, authorization and observability.

## Example layered flow

```text
HTTP Controller
      |
      v
Application Service
      |
      v
Domain Model / Policies
      |
      v
Repository or Gateway Contract
      |
      v
Infrastructure Adapter
```

The exact layers depend on the application. A small application does not need every layer as a separate package.

## Benefits

- Changes to transport do not automatically change business rules.
- Domain logic can be tested without starting infrastructure.
- Persistence technology can change behind a suitable boundary.
- Responsibilities and ownership become easier to understand.

## Common failure modes

- Anemic layers that only forward calls without adding value.
- Business rules duplicated in controllers and persistence code.
- A generic `Utils` or `Common` module becoming a dumping ground.
- Circular dependencies between layers.
- Applying a rigid layered architecture to trivial functionality.

## Guidance

Separate concerns where they change for different reasons or require different testing and deployment boundaries. Keep the architecture proportional to the problem.
