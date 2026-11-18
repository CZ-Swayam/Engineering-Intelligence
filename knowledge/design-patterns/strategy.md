---
id: design-patterns.strategy
title: Strategy Pattern
category: architecture
tags:
- design-patterns
- behavioral-pattern
- polymorphism
technologies: []
layers:
- application
- domain
patterns:
- strategy
summary: The Strategy pattern encapsulates interchangeable algorithms behind a common
  contract and lets a client select or receive the required behavior.
related_components: []
references: []
last_reviewed: '2026-11-18'
status: published
---

# Strategy Pattern

## Intent

Encapsulate a family of algorithms behind a common interface so they can be selected or replaced independently of the client that uses them.

## Example

A shipping service may support standard, express and international shipping calculations.

```text
ShippingStrategy
  calculateCost(order)

StandardShipping
ExpressShipping
InternationalShipping

CheckoutService
  - shippingStrategy
```

`CheckoutService` delegates cost calculation to the selected strategy rather than containing a growing chain of shipping-specific conditionals.

## When to use

- Several algorithms implement the same conceptual operation.
- The algorithm may vary by configuration, customer, context or runtime choice.
- Conditional logic is growing and each branch changes independently.

## When not to use

- There is only one stable algorithm.
- A simple conditional is clearer.
- The abstraction would add more complexity than the variation warrants.

## Trade-offs

Strategy improves extensibility and test isolation, but introduces more types and requires a selection mechanism. Keep strategy selection separate from the algorithm implementation when that makes the design clearer.

## Related principles

Strategy commonly supports Open/Closed Principle and composition over inheritance.
