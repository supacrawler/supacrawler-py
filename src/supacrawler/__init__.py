from .client import (
    SupacrawlerClient, 
    SupacrawlerError,
    SupacrawlerBadRequestError,
    SupacrawlerForbiddenError,
    SupacrawlerNotFoundError,
    SupacrawlerTimeoutError,
    SupacrawlerUnprocessableError,
    SupacrawlerRateLimitError,
    SupacrawlerServerError,
)
from .types import (
    WatchCreateRequest,
    WatchCreateResponse,
    WatchDeleteResponse,
    WatchGetResponse,
    WatchListResponse,
)

# Export commonly used generated models for convenience
from .scraper_client.models import (
    ScrapeResponse,
    ScrapeMetadata,
    PageContent,
    PageMetadata,
    CrawlCreateRequest,
    CrawlStatusResponse,
    ParseCreateRequest,
    ParseResponse,
    ParseCreateRequestOutputFormat,
)

__all__ = [
    "SupacrawlerClient",
    "SupacrawlerError",
    "SupacrawlerBadRequestError",
    "SupacrawlerForbiddenError", 
    "SupacrawlerNotFoundError",
    "SupacrawlerTimeoutError",
    "SupacrawlerUnprocessableError",
    "SupacrawlerRateLimitError",
    "SupacrawlerServerError",
    "WatchCreateRequest",
    "WatchCreateResponse",
    "WatchGetResponse",
    "WatchListResponse",
    "WatchDeleteResponse",
    # Generated models for direct use
    "ScrapeResponse",
    "ScrapeMetadata", 
    "PageContent",
    "PageMetadata",
    "CrawlCreateRequest",
    "CrawlStatusResponse",
    "ParseCreateRequest",
    "ParseResponse",
    "ParseCreateRequestOutputFormat",
]
