---
id: architecture.lld-fundamentals
title: Low-Level Design Fundamentals
category: architecture
tags:
- lld
- object-oriented-design
- software-design
- maintainability
technologies: []
layers:
- application
- domain
- infrastructure
- cross-cutting
patterns: []
summary: Low-level design translates system requirements into concrete classes, interfaces,
  responsibilities, collaborations, data structures and interaction flows.
related_components: []
references: []
last_reviewed: '2026-11-18'
status: published
---

# Low-Level Design Fundamentals

## Purpose

Low-level design (LLD) describes how a system or feature will be implemented internally. It bridges high-level architecture and code. It should make responsibilities, object boundaries, interactions, data ownership and important failure cases understandable before implementation.

## What an LLD should answer

- What are the main objects, modules or services?
- What responsibility does each own?
- Which interfaces do they expose?
- How do objects collaborate to complete a use case?
- Where does state live, and who may change it?
- What are the important invariants and validation rules?
- How are errors, retries, concurrency and external dependencies handled?
- How can the design be tested?

## A practical design sequence

1. Clarify functional requirements and quality attributes.
2. Identify use cases and important scenarios.
3. Identify domain concepts, entities and value objects.
4. Assign responsibilities and define boundaries.
5. Define interfaces and collaboration flows.
6. Choose data structures and persistence boundaries.
7. Apply patterns only where they simplify a real variation or collaboration.
8. Review failure paths, concurrency and security.
9. Validate the design against testability and change scenarios.

## Useful design artifacts

Depending on complexity, an LLD may include:
- Class or component diagrams.
- Sequence diagrams for important use cases.
- State diagrams for lifecycle-heavy objects.
- API and interface contracts.
- Data models and invariants.
- Error and retry behavior.
- Key design decisions and alternatives.

Do not create diagrams merely to fill a document. Use the smallest set of artifacts that makes the design unambiguous.

## Example: order placement

A simple order workflow might involve `OrderController`, `PlaceOrderService`, `InventoryGateway`, `PaymentGateway`, `OrderRepository` and domain objects such as `Order` and `OrderLine`.

The controller handles transport concerns. The application service coordinates the use case. Domain objects protect business invariants. Gateways isolate external systems. The repository abstracts persistence where that abstraction provides value.

## Common mistakes

- Designing classes before understanding use cases.
- Creating a class for every noun in a requirement.
- Mixing transport, business rules and persistence in one class.
- Using patterns by name rather than solving a concrete problem.
- Ignoring failure paths and concurrent requests.
- Overengineering speculative future requirements.

## Review checklist

A good LLD has clear responsibilities, explicit contracts, controlled state changes, low unnecessary coupling, testable boundaries and enough detail to implement without guessing.
