---
id: architecture.composition-over-inheritance
title: Composition Over Inheritance
category: architecture
tags:
- composition
- inheritance
- oop
- object-design
technologies: []
layers:
- application
- domain
patterns: []
summary: Composition builds behavior by combining collaborating objects and is often
  more flexible than deep inheritance hierarchies.
related_components: []
references: []
last_reviewed: '2026-11-18'
status: published
---

# Composition Over Inheritance

## The idea

Inheritance models an is-a relationship and reuses behavior through a subtype hierarchy. Composition builds an object from collaborators that provide specific behavior.

Prefer composition when behavior needs to vary independently, be replaced at runtime or be reused by otherwise unrelated types.

## Example

A `ReportService` can compose a `ReportFormatter` and a `ReportRepository`:

```text
ReportService
  - formatter: ReportFormatter
  - repository: ReportRepository
```

A PDF formatter and CSV formatter can implement the same contract. The service does not need a subclass for every formatter/repository combination.

## Benefits

- Collaborators can be replaced independently.
- Behavior can be assembled without a rigid class hierarchy.
- Dependencies are visible.
- Unit tests can substitute focused collaborators.
- Avoids fragile base-class coupling.

## When inheritance is appropriate

Inheritance can be useful when there is a genuine subtype relationship and the subtype can honor the base type's behavioral contract. A small, stable hierarchy can be clearer than composition.

## Warning signs

- Deep inheritance trees.
- Subclasses overriding methods merely to disable behavior.
- Base classes accumulating hooks for unrelated use cases.
- Changes to a base class breaking distant subclasses.
- Class names representing combinations of features.

## Rule of thumb

Use inheritance to model a true substitutable subtype. Use composition to assemble capabilities and delegate work. Neither is universally superior; choose the simpler model that preserves clear contracts.
