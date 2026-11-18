---
id: design-patterns.adapter
title: Adapter Pattern
category: architecture
tags:
- design-patterns
- structural-pattern
- integration
technologies: []
layers:
- application
- infrastructure
patterns:
- adapter
summary: The Adapter pattern translates one interface into another interface expected
  by a client, allowing incompatible systems to collaborate.
related_components: []
references: []
last_reviewed: '2026-11-18'
status: published
---

# Adapter Pattern

## Intent

Convert an existing interface into the contract expected by a client without changing the client or the adaptee.

## Example

An application expects:

```text
PaymentGateway.charge(amount, currency)
```

A third-party provider exposes a different SDK method and response structure. `ProviderPaymentAdapter` implements the application's contract, translates the request, invokes the provider and maps the response.

## When to use

- Integrating a third-party SDK or legacy API.
- Isolating vendor-specific types from domain/application code.
- Migrating between implementations while preserving a stable internal contract.
- Wrapping a subsystem with a simpler interface.

## Benefits and trade-offs

Adapters isolate external changes and make integrations easier to test. They add a translation layer, so avoid creating adapters that simply forward calls without resolving a real mismatch or boundary.

## Important details

Translate errors deliberately, preserve relevant semantics, handle timeouts and retries at the correct boundary, and avoid leaking provider-specific objects through the application contract.
