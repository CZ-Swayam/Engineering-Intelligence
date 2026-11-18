---
id: architecture.solid-principles
title: SOLID Design Principles
category: architecture
tags:
- solid
- oop
- maintainability
- object-oriented-design
technologies: []
layers:
- application
- domain
- infrastructure
patterns:
- solid
summary: SOLID is a set of five object-oriented design principles intended to make
  software easier to change, extend and test.
related_components: []
references: []
last_reviewed: '2026-11-18'
status: published
---

# SOLID Design Principles

SOLID is a commonly used set of object-oriented design heuristics. It is not a checklist that every class must mechanically satisfy; use the principles to identify design pressure and reduce costly coupling.

## 1. Single Responsibility Principle (SRP)

A module should have one cohesive responsibility and one primary reason to change.

A class that validates an order, calculates tax, writes to a database and sends email has several unrelated reasons to change. Separate responsibilities where they evolve independently.

**Review question:** Are unrelated changes repeatedly forcing edits to this class?

## 2. Open/Closed Principle (OCP)

Software entities should be open to extension while minimizing modification to stable, tested code.

For example, a pricing service can depend on a `DiscountPolicy` interface. Adding a new discount policy then introduces a new implementation rather than adding another conditional branch to the pricing service.

Do not introduce abstractions for every hypothetical variation. OCP is most useful around variation that is real or reasonably expected.

## 3. Liskov Substitution Principle (LSP)

A subtype should be usable wherever its base type is expected without breaking the base type's behavioral promises.

A subtype must preserve relevant preconditions, postconditions and invariants. If a subclass rejects inputs that the parent accepts or changes expected behavior, the inheritance relationship may be invalid.

## 4. Interface Segregation Principle (ISP)

Clients should not be forced to depend on methods they do not use.

Prefer focused interfaces such as `Readable`, `Writable` and `Searchable` over a large interface that forces every implementation to provide unrelated operations.

## 5. Dependency Inversion Principle (DIP)

High-level policy should not depend directly on low-level implementation details. Both should depend on abstractions owned by the policy boundary.

For example, an application service can depend on `PaymentGateway`, while a Stripe-specific adapter implements that interface.

DIP is about dependency direction; dependency injection is one technique for supplying the implementation.

## Applying SOLID pragmatically

- Start with clear responsibilities and cohesive modules.
- Introduce interfaces at meaningful boundaries, especially where implementations vary or external systems are involved.
- Prefer composition when behavior needs to be assembled.
- Avoid abstractions that only add indirection.
- Revisit the design when changes repeatedly affect unrelated modules.

## Review questions

1. Does this class have multiple unrelated reasons to change?
2. Do new variants require editing stable decision logic?
3. Can every subtype honor the behavior promised by its parent?
4. Are clients coupled to methods they do not need?
5. Do business policies depend on infrastructure details?
