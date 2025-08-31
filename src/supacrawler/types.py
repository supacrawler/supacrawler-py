from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field


class IndexableDict(dict):
    """Dict that can be accessed by index like a list"""

    def __getitem__(self, key: Union[str, int, slice]) -> Any:
        # If key is int -> act like list
        if isinstance(key, int):
            return list(self.values())[key]
        # If key is slice -> return list of values
        elif isinstance(key, slice):
            return list(self.values())[key]
        # Normal dict access
        return super().__getitem__(key)

    def get_key(self, index: int) -> str:
        """Get the key by index"""
        return list(self.keys())[index]

    def first(self) -> Any:
        """Get first value"""
        if not self:
            raise IndexError("IndexableDict is empty")
        return self[0]

    def last(self) -> Any:
        """Get last value"""
        if not self:
            raise IndexError("IndexableDict is empty")
        return self[-1]


# Watch and lightweight friendly wrappers for engine responses

# ------------ Watch ------------


class WatchCreateRequest(BaseModel):
    url: str
    frequency: str
    notify_email: Optional[str] = None
    notification_preference: Optional[str] = None  # 'changes_only' | 'all_runs'
    selector: Optional[str] = None
    include_html: Optional[bool] = None
    include_image: Optional[bool] = None
    full_page: Optional[bool] = None
    quality: Optional[int] = None
    custom_frequency: Optional[str] = None

    def to_json(self) -> Dict[str, Any]:
        """Convert to JSON dict - consistent across all models"""
        return self.model_dump()


class WatchCreateResponse(BaseModel):
    success: bool
    watch_id: str
    message: Optional[str] = None

    def to_json(self) -> Dict[str, Any]:
        """Convert to JSON dict - consistent across all models"""
        return self.model_dump()


class Watch(BaseModel):
    id: Optional[str] = None
    user_id: Optional[str] = None
    url: Optional[str] = None
    frequency: Optional[str] = None
    notify_email: Optional[str] = None
    notification_preference: Optional[str] = None
    include_html: Optional[bool] = None
    include_image: Optional[bool] = None
    full_page: Optional[bool] = None
    quality: Optional[int] = None
    selector: Optional[str] = None
    last_check: Optional[str] = None
    last_notification: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    cron_job_name: Optional[str] = None

    def to_json(self) -> Dict[str, Any]:
        """Convert to JSON dict - consistent across all models"""
        return self.model_dump()


class WatchResult(BaseModel):
    id: Optional[str] = None
    executed_at: Optional[str] = None
    has_changed: Optional[bool] = None
    change_type: Optional[str] = None
    content_hash: Optional[str] = None
    content: Optional[str] = None
    html_content: Optional[str] = None
    image_url: Optional[str] = None

    def to_json(self) -> Dict[str, Any]:
        """Convert to JSON dict - consistent across all models"""
        return self.model_dump()


class WatchGetResponse(BaseModel):
    success: bool
    watch: Optional[Watch] = None
    results: Optional[List[WatchResult]] = None

    def to_json(self) -> Dict[str, Any]:
        """Convert to JSON dict - consistent across all models"""
        return self.model_dump()


class WatchListResponse(BaseModel):
    success: bool
    total: Optional[int] = None
    watches: List[Watch] = Field(default_factory=list)

    def to_json(self) -> Dict[str, Any]:
        """Convert to JSON dict - consistent across all models"""
        return self.model_dump()


class WatchDeleteResponse(BaseModel):
    success: bool
    message: Optional[str] = None

    def to_json(self) -> Dict[str, Any]:
        """Convert to JSON dict - consistent across all models"""
        return self.model_dump()


# ------------ Screenshot (friendly wrappers) ------------


class ScreenshotJob(BaseModel):
    success: bool
    job_id: Optional[str] = None
    status: Optional[str] = None
    url: Optional[str] = None
    screenshot_url: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

    def to_json(self) -> Dict[str, Any]:
        """Convert to JSON dict - consistent across all models"""
        return self.model_dump()

    @classmethod
    def from_engine(cls, resp) -> ScreenshotJob:
        # Handle generated screenshot responses
        from .scraper_client.types import UNSET

        success = getattr(resp, "success", False)
        job_id = getattr(resp, "job_id", None)
        status = getattr(resp, "status", None)
        url = getattr(resp, "url", None)
        screenshot_url = getattr(resp, "screenshot", None)
        metadata_obj = getattr(resp, "metadata", None)

        # Handle UNSET values
        if job_id is UNSET:
            job_id = None
        if status is UNSET:
            status = None
        elif hasattr(status, "value"):
            status = status.value
        if url is UNSET:
            url = None
        if screenshot_url is UNSET:
            screenshot_url = None
        
        # Handle metadata
        metadata = None
        if metadata_obj is not UNSET and metadata_obj is not None:
            # Convert metadata object to dict
            if hasattr(metadata_obj, "to_dict"):
                metadata = metadata_obj.to_dict()
            else:
                # Extract basic metadata fields
                metadata = {}
                for field in ["width", "height", "format_", "file_size", "load_time"]:
                    value = getattr(metadata_obj, field, None)
                    if value is not UNSET and value is not None:
                        # Clean up field names (format_ -> format)
                        clean_field = field.replace("_", "") if field.endswith("_") else field
                        metadata[clean_field] = value

        return cls(
            success=success,
            job_id=job_id,
            status=status,
            url=url,
            screenshot_url=screenshot_url,
            metadata=metadata,
        )


# ------------ Crawl (friendly wrappers) ------------


class PageMetadata(BaseModel):
    title: Optional[str] = None
    status_code: Optional[int] = None
    description: Optional[str] = None
    language: Optional[str] = None
    robots: Optional[str] = None

    # Allow arbitrary additional metadata fields
    model_config = {"extra": "allow"}

    def to_json(self) -> Dict[str, Any]:
        """Convert to JSON dict - consistent across all models"""
        return self.model_dump()


class Page(BaseModel):
    markdown: Optional[str] = None
    html: Optional[str] = None
    links: Optional[List[str]] = None
    metadata: Optional[PageMetadata] = None

    def to_json(self) -> Dict[str, Any]:
        """Convert to JSON dict - consistent across all models"""
        return self.model_dump()


class CrawlStats(BaseModel):
    total_pages: Optional[int] = None
    successful_pages: Optional[int] = None
    failed_pages: Optional[int] = None

    def to_json(self) -> Dict[str, Any]:
        """Convert to JSON dict - consistent across all models"""
        return self.model_dump()


class CrawlData(BaseModel):
    model_config = {"arbitrary_types_allowed": True}

    url: Optional[str] = None
    pages: IndexableDict = Field(default_factory=IndexableDict)
    errors: Dict[str, str] = Field(default_factory=dict)
    stats: Optional[CrawlStats] = None
    render_js: Optional[bool] = None

    # Back-compat alias used in examples: final.data.crawl_data
    @property
    def crawl_data(self) -> IndexableDict:
        return self.pages

    def __len__(self) -> int:  # allows len(final.data)
        return len(self.pages)

    def to_json(self) -> Dict[str, Any]:
        """Convert to JSON dict - consistent across all models"""
        return self.model_dump()

    @classmethod
    def from_engine(cls, data) -> CrawlData:
        # Handle None/empty data gracefully
        if data is None:
            return cls()

        # Handle UNSET values
        try:
            from .scraper_client.types import UNSET, Unset

            if data is UNSET or isinstance(data, Unset):
                return cls()
        except ImportError:
            pass

        # Build pages dict from crawl data
        pages: IndexableDict = IndexableDict()
        crawl_data = getattr(data, "crawl_data", None)
        if crawl_data is not None:
            crawl_props = getattr(crawl_data, "additional_properties", None)
            if isinstance(crawl_props, dict):
                for url, page_content in crawl_props.items():
                    # Extract content
                    markdown = getattr(page_content, "markdown", "")
                    html = getattr(page_content, "html", None)

                    # Handle UNSET in content
                    try:
                        from .scraper_client.types import UNSET, Unset

                        if markdown is UNSET or isinstance(markdown, Unset):
                            markdown = ""
                        if html is UNSET or isinstance(html, Unset):
                            html = None
                    except ImportError:
                        pass

                    # Extract and build metadata object
                    page_metadata = None
                    raw_metadata = getattr(page_content, "metadata", None)
                    if raw_metadata is not None:
                        # Build metadata dict from the raw metadata object
                        metadata_dict = {}

                        # Extract common fields
                        for field in ["title", "status_code", "description", "language", "robots"]:
                            value = getattr(raw_metadata, field, None)
                            # Handle UNSET values
                            try:
                                from .scraper_client.types import UNSET, Unset

                                if value is UNSET or isinstance(value, Unset):
                                    value = None
                            except ImportError:
                                pass
                            if value is not None:
                                metadata_dict[field] = value

                        # Add any additional properties if available
                        additional = getattr(raw_metadata, "additional_properties", {})
                        if isinstance(additional, dict):
                            metadata_dict.update(additional)

                        # Create PageMetadata object if we have any metadata
                        if metadata_dict:
                            page_metadata = PageMetadata(**metadata_dict)

                    pages[url] = Page(
                        markdown=markdown if markdown else None,
                        html=html,
                        links=None,  # Crawl data doesn't have links format
                        metadata=page_metadata,
                    )

        # Build errors dict
        errors: Dict[str, str] = {}
        error_data = getattr(data, "error_data", None)
        if error_data is not None:
            error_props = getattr(error_data, "additional_properties", None)
            if isinstance(error_props, dict):
                errors = dict(error_props)

        # Build stats
        stats = None
        statistics = getattr(data, "statistics", None)
        if statistics is not None:
            stats = CrawlStats(
                total_pages=getattr(statistics, "total_pages", None),
                successful_pages=getattr(statistics, "successful_pages", None),
                failed_pages=getattr(statistics, "failed_pages", None),
            )

        # Handle render_js
        render_js = getattr(data, "render_js", None)
        try:
            from .scraper_client.types import UNSET, Unset

            if render_js is UNSET or isinstance(render_js, Unset):
                render_js = None
        except ImportError:
            pass

        return cls(
            url=getattr(data, "url", None),
            pages=pages,
            errors=errors,
            stats=stats,
            render_js=render_js,
        )


class CrawlJob(BaseModel):
    success: bool
    job_id: Optional[str] = None
    status: Optional[str] = None
    data: Optional[CrawlData] = None
    error: Optional[str] = None

    def to_json(self) -> Dict[str, Any]:
        """Convert to JSON dict - consistent across all models"""
        return self.model_dump()

    @classmethod
    def from_engine(cls, resp) -> CrawlJob:
        # Handle data gracefully
        data = getattr(resp, "data", None)
        wrapped: Optional[CrawlData] = None

        # Handle UNSET data
        try:
            from .scraper_client.types import UNSET, Unset

            if data is not UNSET and not isinstance(data, Unset) and data is not None:
                wrapped = CrawlData.from_engine(data)
        except ImportError:
            if data is not None:
                wrapped = CrawlData.from_engine(data)

        # Handle status
        status_val = getattr(resp, "status", None)
        status_str = None
        if status_val is not None:
            try:
                from .scraper_client.types import UNSET, Unset

                if status_val is not UNSET and not isinstance(status_val, Unset):
                    status_str = getattr(status_val, "value", str(status_val))
            except ImportError:
                status_str = getattr(status_val, "value", str(status_val))

        # Handle job_id
        job_id = getattr(resp, "job_id", None)
        try:
            from .scraper_client.types import UNSET, Unset

            if job_id is UNSET or isinstance(job_id, Unset):
                job_id = None
        except ImportError:
            pass

        # Handle error
        error = getattr(resp, "error", None)
        try:
            from .scraper_client.types import UNSET, Unset

            if error is UNSET or isinstance(error, Unset):
                error = None
        except ImportError:
            pass

        return cls(
            success=bool(getattr(resp, "success", False)),
            job_id=job_id,
            status=status_str,
            data=wrapped,
            error=error,
        )
