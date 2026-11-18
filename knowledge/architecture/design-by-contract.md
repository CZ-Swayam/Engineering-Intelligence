---
id: architecture.design-by-contract
title: Design by Contract
category: architecture
tags:
- contracts
- preconditions
- postconditions
- invariants
technologies: []
layers:
- application
- domain
patterns: []
summary: Design by Contract makes operation expectations explicit through preconditions,
  postconditions and invariants.
related_components: []
references: []
last_reviewed: '2026-11-18'
status: published
---

# Design by Contract

## Core concepts

Design by Contract describes software behavior using explicit obligations and guarantees.

- Preconditions: what must be true before an operation is called.
- Postconditions: what the operation guarantees if it completes successfully.
- Invariants: conditions that must remain true for an object or system state.

## Example: bank withdrawal

For `withdraw(amount)`:
- Preconditions: amount is positive; account is open.
- Postconditions: balance is reduced by the amount if the operation succeeds.
- Invariant: balance must not fall below the permitted overdraft limit.

The operation should define what happens when a precondition is not met, such as a domain exception or validation result.

## Why it helps

- Makes assumptions visible.
- Improves API and class design.
- Gives tests concrete properties to verify.
- Reduces ambiguity between callers and implementations.

## Practical use

Contracts can be documented, checked through runtime validation, encoded in types where possible and verified with tests. Avoid relying on comments alone for critical invariants.

For external input, validate at the system boundary. For internal domain operations, preserve invariants in the domain model rather than trusting every caller to remember them.
