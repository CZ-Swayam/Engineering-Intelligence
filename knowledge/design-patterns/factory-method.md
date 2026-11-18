---
id: design-patterns.factory-method
title: Factory Method Pattern
category: architecture
tags:
- design-patterns
- creational-pattern
- object-creation
technologies: []
layers:
- application
- infrastructure
patterns:
- factory-method
summary: Factory Method delegates object creation to a dedicated method or creator
  so callers do not need to know concrete construction details.
related_components: []
references: []
last_reviewed: '2026-11-18'
status: published
---

# Factory Method Pattern

## Intent

Provide a creation point that lets a system choose which concrete object to instantiate without spreading construction decisions across callers.

## Example

A document exporter may create a `PdfExporter` or `CsvExporter` based on an export format.

```text
ExporterFactory.create(format) -> Exporter
```

The caller uses the `Exporter` contract and does not need to know each implementation's constructor details.

## When to use

- Creation logic is non-trivial or repeated.
- The concrete type depends on configuration or input.
- Callers should be decoupled from implementation classes.
- Construction needs validation or setup.

## When not to use

- Construction is simple and stable.
- A direct constructor is clearer.
- The factory merely renames `new` without adding a useful boundary.

## Factory Method versus Abstract Factory

Factory Method typically provides a creation hook for one product abstraction. Abstract Factory provides a contract for creating a family of related products.

Terminology is sometimes used loosely in codebases; document the actual responsibility rather than relying only on the pattern name.
