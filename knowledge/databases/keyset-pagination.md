---
id: database.keyset-pagination
title: Keyset Pagination
category: database
tags:
  - pagination
  - performance
  - large-datasets
technologies:
  - postgresql
  - sql-server
  - azure-synapse
layers:
  - application
  - infrastructure
patterns:
  - keyset-pagination
summary: Keyset pagination retrieves the next page relative to the last-seen sort key instead of calculating and skipping an offset.
related_components:
  - backend.pagination
references:
  - https://learn.microsoft.com/en-us/azure/synapse-analytics/sql-data-warehouse/sql-data-warehouse-tables-overview
last_reviewed: "2026-11-18"
status: published
---

# Keyset Pagination

## Problem

Deep offset pagination (`OFFSET n LIMIT m`) can become expensive because the database may need to locate and skip an increasing number of rows. Inserts and deletes can also shift page boundaries between requests.

## How it works

Use the last row's sort key as the cursor for the next query. For a stable ascending order on `created_at` and unique `id`:

```sql
SELECT id, created_at, payload
FROM records
WHERE created_at > :last_created_at
   OR (created_at = :last_created_at AND id > :last_id)
ORDER BY created_at ASC, id ASC
FETCH FIRST :page_size ROWS ONLY;
```

Syntax varies by database. Use a deterministic order, include a unique tie-breaker, create a supporting index, validate cursor input, and define nullable-key behavior.

## When to use

- Large datasets and deep sequential navigation.
- APIs where arbitrary page-number jumps are not required.
- Workloads where predictable query cost matters.

## Trade-offs

Keyset pagination avoids increasingly large offsets, but arbitrary page jumps are difficult and cursor encoding adds complexity. Previous-page navigation requires reverse ordering logic.

## Database considerations

Validate SQL syntax, indexing, ordering guarantees and execution plans on the target database. Do not assume OLTP behavior transfers directly to an analytical warehouse.

## Related component

See `backend.pagination`.
