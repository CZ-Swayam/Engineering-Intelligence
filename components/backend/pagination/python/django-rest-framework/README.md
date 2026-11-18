# Django REST Framework pagination examples

```python
from rest_framework.pagination import PageNumberPagination, CursorPagination

class StandardPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = "page_size"
    max_page_size = 200

class RecordCursorPagination(CursorPagination):
    page_size = 50
    ordering = ("created_at", "id")
```

Use deterministic ordering and verify model fields and indexes. These are integration examples, not a published package.
