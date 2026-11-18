package example.pagination;

import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;

/** Bounded, deterministic offset pagination defaults. */
public final class PaginationDefaults {
    public static final int DEFAULT_PAGE_SIZE = 50;
    public static final int MAX_PAGE_SIZE = 200;

    private PaginationDefaults() {}

    public static Pageable create(int page, int requestedSize) {
        if (page < 0) {
            throw new IllegalArgumentException("page must be zero or greater");
        }
        int size = Math.max(1, Math.min(requestedSize, MAX_PAGE_SIZE));
        return PageRequest.of(
            page,
            size,
            Sort.by(Sort.Order.asc("createdAt"), Sort.Order.asc("id"))
        );
    }
}
