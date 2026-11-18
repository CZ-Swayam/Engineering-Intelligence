---
id: architecture.cohesion-and-coupling
title: Cohesion and Coupling
category: architecture
tags:
- cohesion
- coupling
- modularity
- maintainability
technologies: []
layers:
- application
- domain
- infrastructure
patterns: []
summary: Good modular design aims for high cohesion within a module and low unnecessary
  coupling between modules.
related_components: []
references: []
last_reviewed: '2026-11-18'
status: published
---

# Cohesion and Coupling

## Cohesion

Cohesion describes how closely the responsibilities inside a module belong together. A highly cohesive module has a clear purpose and its elements collaborate toward that purpose.

For example, an invoice calculator that contains tax, line-total and discount calculations is more cohesive than a general utility class containing unrelated invoice, email and file operations.

## Coupling

Coupling describes how much one module depends on the details or behavior of another. Some coupling is necessary; the goal is to minimize unnecessary and unstable dependencies.

Tight coupling appears when a caller knows another module's internal data structures, construction details or many implementation-specific operations.

## Design goals

- Keep related behavior together.
- Expose small, stable contracts.
- Depend on abstractions at boundaries where implementations vary.
- Avoid shared mutable state across modules.
- Keep dependency direction intentional.
- Prefer explicit data flow over hidden global dependencies.

## Trade-off

Extremely low coupling is not an end in itself. Too many tiny modules and interfaces can make a system harder to understand. A good boundary balances cohesion, change isolation and navigability.

## Review questions

- Can this module be described with one clear purpose?
- Do its methods operate on the same concepts?
- Does a change in one module force unrelated modules to change?
- Are callers depending on implementation details?
- Is the abstraction reducing complexity or merely adding indirection?
