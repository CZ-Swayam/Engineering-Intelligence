---
id: design-patterns.builder
title: Builder Pattern
category: architecture
tags:
- design-patterns
- creational-pattern
- object-construction
technologies: []
layers:
- application
- domain
patterns:
- builder
summary: The Builder pattern separates the construction of a complex object from its
  final representation and makes multi-step configuration easier to express.
related_components: []
references: []
last_reviewed: '2026-11-18'
status: published
---

# Builder Pattern

## Intent

Build an object through a sequence of explicit configuration steps, especially when it has many optional parameters or construction rules.

## Example

```text
ReportRequest.builder()
  .withDateRange(range)
  .includeArchived(false)
  .withFormat(PDF)
  .build()
```

The builder can validate that required values are present and that combinations are valid before returning the final object.

## When to use

- Constructors have many parameters.
- Many options are optional.
- Construction has multiple steps.
- The object should be immutable after creation.
- Named configuration steps improve readability.

## When not to use

- The object has only a few simple required fields.
- A constructor or language-native data class is already clear.
- The builder duplicates validation without adding value.

## Design considerations

- Make required versus optional fields explicit.
- Validate cross-field constraints in `build()`.
- Decide whether a builder is reusable or single-use.
- Avoid a fluent API that hides important side effects.
