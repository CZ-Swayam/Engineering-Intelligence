---
id: architecture.encapsulation-and-abstraction
title: Encapsulation and Abstraction
category: architecture
tags:
- encapsulation
- abstraction
- oop
- object-design
technologies: []
layers:
- domain
- application
patterns: []
summary: Encapsulation protects an object's state and invariants, while abstraction
  exposes essential behavior and hides implementation details.
related_components: []
references: []
last_reviewed: '2026-11-18'
status: published
---

# Encapsulation and Abstraction

## Encapsulation

Encapsulation keeps state and the operations that maintain its correctness together. An object should control how its internal state changes instead of exposing mutable fields for arbitrary modification.

For example, an `Account` should expose `deposit(amount)` and `withdraw(amount)` rather than allowing callers to assign any value to `balance`.

```text
Account
  private balance
  deposit(amount)
  withdraw(amount)
  getBalance()
```

The object can reject non-positive deposits and withdrawals that violate its overdraft rule. This keeps the invariant close to the state it protects.

## Abstraction

Abstraction exposes a useful contract while hiding details that callers do not need to know.

A caller may depend on `NotificationSender.send(message)` without knowing whether the implementation uses email, SMS or a queue.

Abstraction is about the boundary and contract, not necessarily an interface keyword. A small concrete class can provide a useful abstraction too.

## How they work together

- Encapsulation protects internal correctness.
- Abstraction limits what other parts of the system need to understand.
- Both reduce accidental coupling and make implementation changes safer.

## Common mistakes

- Public mutable state that allows invalid object states.
- Getters and setters for every field without meaningful invariants.
- Interfaces that expose implementation details.
- Excessive abstraction that makes simple behavior difficult to follow.

## Design guidance

Expose operations that express intent, not just storage mechanics. Keep invariants inside the object or aggregate responsible for them. Make the public contract smaller than the internal implementation.
