---
id: architecture.dependency-injection
title: Dependency Injection
category: architecture
tags:
- dependency-injection
- dependency-management
- testability
- coupling
technologies: []
layers:
- application
- infrastructure
patterns:
- dependency-injection
summary: Dependency injection supplies an object with the collaborators it needs instead
  of making it construct concrete dependencies internally.
related_components: []
references: []
last_reviewed: '2026-11-18'
status: published
---

# Dependency Injection

## Definition

Dependency injection (DI) is a technique in which an object receives its dependencies from the outside. The object focuses on its responsibility rather than locating or constructing infrastructure collaborators.

## Example

Instead of constructing a concrete payment provider inside a service:

```text
OrderService
  constructor(paymentGateway, orderRepository)
```

The application composition root supplies implementations:

```text
OrderService(
  StripePaymentGateway,
  SqlOrderRepository
)
```

The service depends on contracts where appropriate; the composition root knows the concrete types.

## Common forms

- Constructor injection: dependencies are supplied when the object is created. Usually the clearest default because required dependencies are explicit.
- Setter injection: dependencies are supplied after construction. Useful for optional dependencies, but can permit partially initialized objects.
- Method injection: a dependency is supplied for one operation rather than retained as object state.

## Benefits

- Makes dependencies visible.
- Supports substituting test doubles.
- Reduces direct coupling to infrastructure construction.
- Centralizes application wiring.

## DI versus Dependency Inversion

Dependency Injection is a mechanism for supplying dependencies. Dependency Inversion is a design principle about the direction of source-code dependencies. DI can help implement DIP, but they are not the same concept.

## Common mistakes

- Injecting a large service locator instead of explicit dependencies.
- Creating interfaces for every class without a real boundary.
- Using field injection where constructor injection would make requirements clearer.
- Building circular dependencies.
- Hiding business logic inside dependency-injection configuration.

## Guidance

Prefer constructor injection for required collaborators. Keep object construction in a composition root or framework configuration. Keep constructors small; a long dependency list can indicate that the class has too many responsibilities.
