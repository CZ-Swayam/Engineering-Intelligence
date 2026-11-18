# Spring Boot pagination example

Spring Data supports offset pagination through `Pageable`. Apply deterministic sorting, including a unique tie-breaker:

```java
PageRequest.of(
    page,
    size,
    Sort.by(Sort.Order.asc("createdAt"), Sort.Order.asc("id"))
);
```

For deep pages over large datasets, assess keyset/seek pagination against the target database and query plan.
