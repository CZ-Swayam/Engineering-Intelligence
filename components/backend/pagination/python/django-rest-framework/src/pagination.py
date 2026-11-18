from rest_framework.pagination import CursorPagination, PageNumberPagination


class StandardPageNumberPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = "page_size"
    max_page_size = 200


class StableRecordCursorPagination(CursorPagination):
    page_size = 50
    ordering = ("created_at", "id")
