---
id: architecture.interface-design
title: Designing Interfaces and Contracts
category: architecture
tags:
- interfaces
- contracts
- api-design
- abstraction
technologies: []
layers:
- application
- domain
- infrastructure
patterns: []
summary: A good interface defines a small, stable and behaviorally clear contract
  between a caller and an implementation.
related_components: []
references: []
last_reviewed: '2026-11-18'
status: published
---

# Designing Interfaces and Contracts

## What an interface should communicate

An interface is a boundary between a caller and an implementation. Its contract should make clear:
- Available operations and their meaning.
- Required inputs and accepted ranges.
- Return values and their guarantees.
- Errors or exceptional conditions.
- Side effects and state changes.
- Thread-safety or concurrency expectations where relevant.

## Design principles

1. Keep the contract focused on one cohesive capability.
2. Prefer intention-revealing names.
3. Avoid exposing internal data structures unnecessarily.
4. Define error behavior explicitly.
5. Avoid methods with ambiguous optional parameters or surprising side effects.
6. Keep compatibility in mind when evolving public contracts.
7. Do not expose methods that most clients cannot meaningfully use.

## Example

A `PaymentGateway` contract might define:

```text
authorize(amount, currency, paymentMethod) -> AuthorizationResult
capture(authorizationId) -> CaptureResult
refund(captureId, amount) -> RefundResult
```

The contract should also define idempotency behavior, failure categories and whether operations can be retried safely.

## Interface versus implementation

Callers should rely on the contract, not assumptions about a particular implementation. An implementation may use HTTP, a database, an in-memory fake or a message broker as long as it honors the contract.

## Avoid interface inflation

Do not create an interface for every class by default. An interface is most valuable at a meaningful variation, testing, module or external-system boundary.
