---
id: architecture.immutability-and-value-objects
title: Immutability and Value Objects
category: architecture
tags:
- immutability
- value-object
- domain-model
- state
technologies: []
layers:
- domain
- application
patterns: []
summary: Immutable objects cannot be changed after creation, while value objects model
  concepts by their values rather than by identity.
related_components: []
references: []
last_reviewed: '2026-11-18'
status: published
---

# Immutability and Value Objects

## Immutability

An immutable object cannot be changed after it has been created. Operations that appear to modify it instead return a new value.

Immutability can reduce accidental state changes, simplify reasoning and make objects safer to share. It is especially useful for configuration, identifiers, money, dates and request/result values.

## Value objects

A value object represents a concept whose meaning is determined by its attributes rather than a unique identity.

Examples include:
- `Money(amount, currency)`
- `EmailAddress(value)`
- `DateRange(start, end)`
- `GeoCoordinate(latitude, longitude)`

Two `Money` values with the same amount and currency are generally equal by value.

## Protect invariants at construction

A `Money` value can reject invalid currency codes or unsupported precision when constructed. A `DateRange` can enforce that its end is not before its start.

This keeps invalid values from spreading through the system.

## Value object versus entity

An entity has identity that remains meaningful even when its attributes change. A value object is identified by its value.

For example, a customer is typically an entity; a customer's postal address may be modeled as a value object.

## Practical guidance

- Prefer immutable value objects when the concept is naturally value-based.
- Validate invariants at construction or through controlled factories.
- Avoid excessive object wrappers that add no domain meaning.
- Consider serialization, persistence and equality semantics explicitly.
