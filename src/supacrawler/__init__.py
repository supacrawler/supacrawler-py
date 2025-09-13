from .client import SupacrawlerClient, SupacrawlerError
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
)

__all__ = [
    "SupacrawlerClient",
    "SupacrawlerError",
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
]
