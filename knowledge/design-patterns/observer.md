---
id: design-patterns.observer
title: Observer Pattern
category: architecture
tags:
- design-patterns
- behavioral-pattern
- events
technologies: []
layers:
- application
- domain
patterns:
- observer
summary: The Observer pattern lets multiple subscribers react to a subject's state
  change or event without the subject depending on their concrete implementations.
related_components: []
references: []
last_reviewed: '2026-11-18'
status: published
---

# Observer Pattern

## Intent

Define a one-to-many relationship so that when a subject publishes an event or state change, interested observers can be notified.

## Example

When an order is placed, observers may update analytics, send a notification or trigger fulfillment.

```text
OrderPlaced event
  -> NotificationHandler
  -> AnalyticsHandler
  -> FulfillmentHandler
```

The order workflow publishes a meaningful event rather than directly depending on every subscriber.

## In-process versus distributed events

An in-process observer mechanism usually runs within one process and may be synchronous. A message broker or event bus introduces distributed delivery concerns such as retries, duplicate messages, ordering and eventual consistency.

Do not treat these as operationally equivalent.

## When to use

- Multiple independent reactions follow one event.
- Publisher and subscribers should remain decoupled.
- Subscribers can be added without changing the publisher.

## Trade-offs and cautions

- Hidden control flow can make debugging harder.
- Synchronous observers can increase request latency.
- Asynchronous delivery may be at-least-once, requiring idempotent consumers.
- Define error isolation, subscription lifecycle and event versioning.
