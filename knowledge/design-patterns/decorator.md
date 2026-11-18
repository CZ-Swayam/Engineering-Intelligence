---
id: design-patterns.decorator
title: Decorator Pattern
category: architecture
tags:
- design-patterns
- structural-pattern
- composition
technologies: []
layers:
- application
- infrastructure
- cross-cutting
patterns:
- decorator
summary: The Decorator pattern adds behavior around an object while preserving the
  same interface, enabling composable cross-cutting behavior.
related_components: []
references: []
last_reviewed: '2026-11-18'
status: published
---

# Decorator Pattern

## Intent

Wrap an object with another object that implements the same contract, adding behavior before or after delegating to the wrapped object.

## Example

A `PaymentGateway` can be wrapped by:
- `LoggingPaymentGateway`
- `MetricsPaymentGateway`
- `RetryingPaymentGateway`

Each decorator implements the same interface and delegates to the next gateway.

## When to use

- Add logging, metrics, caching or carefully bounded retry behavior.
- Combine optional behaviors without creating many subclasses.
- Extend an object without modifying its original implementation.

## Trade-offs

Decorators compose well, but long wrapper chains can make execution order and debugging harder. Document ordering when behavior depends on it.

## Cautions

- Do not retry non-idempotent operations without an idempotency strategy.
- Avoid logging secrets or sensitive payment data.
- Ensure exceptions and return semantics remain consistent with the wrapped contract.
