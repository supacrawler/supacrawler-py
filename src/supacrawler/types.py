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


class ResponseWrapper:
    """Wrapper for generated response models to add convenience methods"""
    
    def __init__(self, response):
        self._response = response
    
    def to_json(self) -> Dict[str, Any]:
        """Convert to JSON dict using the underlying model's to_dict method"""
        if hasattr(self._response, 'to_dict'):
            return self._response.to_dict()
        return {}
    
    def __getattr__(self, name):
        """Delegate all other attribute access to the underlying response"""
        return getattr(self._response, name)


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


# ------------ Scrape & Crawl (user-friendly wrappers) ------------

class PageMetadata:
    """User-friendly wrapper around generated PageMetadata/ScrapeMetadata models"""
    
    def __init__(self, generated_metadata):
        """Initialize with a generated PageMetadata or ScrapeMetadata"""
        self._metadata = generated_metadata
    
    def to_json(self) -> Dict[str, Any]:
        """Convert to JSON dict - consistent across all models"""
        if hasattr(self._metadata, 'to_dict'):
            return self._metadata.to_dict()
        return {}
    
    def __getattr__(self, name):
        """Delegate attribute access to the underlying generated model"""
        if self._metadata is None:
            return None
        
        from .scraper_client.types import UNSET
        value = getattr(self._metadata, name, None)
        if value is UNSET:
            return None
        return value
    
    @property
    def title(self) -> Optional[str]:
        return self._get_field("title")
    
    @property 
    def status_code(self) -> Optional[int]:
        return self._get_field("status_code")
    
    @property
    def description(self) -> Optional[str]:
        return self._get_field("description")
    
    @property
    def language(self) -> Optional[str]:
        return self._get_field("language")
    
    @property
    def canonical(self) -> Optional[str]:
        return self._get_field("canonical")
        
    @property
    def favicon(self) -> Optional[str]:
        return self._get_field("favicon")
    
    @property
    def og_title(self) -> Optional[str]:
        return self._get_field("og_title")
        
    @property
    def og_description(self) -> Optional[str]:
        return self._get_field("og_description")
    
    @property
    def og_image(self) -> Optional[str]:
        return self._get_field("og_image")
    
    @property
    def og_site_name(self) -> Optional[str]:
        return self._get_field("og_site_name")
    
    @property
    def twitter_title(self) -> Optional[str]:
        return self._get_field("twitter_title")
    
    @property
    def twitter_description(self) -> Optional[str]:
        return self._get_field("twitter_description")
    
    @property
    def twitter_image(self) -> Optional[str]:
        return self._get_field("twitter_image")
    
    @property
    def source_url(self) -> Optional[str]:
        return self._get_field("source_url")
    
    def _get_field(self, field_name):
        """Helper to get field from generated model handling UNSET"""
        if self._metadata is None:
            return None
        
        from .scraper_client.types import UNSET
        value = getattr(self._metadata, field_name, None)
        if value is UNSET:
            return None
        return value
    
    @classmethod
    def from_generated(cls, metadata):
        """Create from generated ScrapeMetadata or PageMetadata"""
        if metadata is None:
            return None
        return cls(metadata)


class Page(BaseModel):
    """User-friendly page wrapper for both scrape and crawl results"""
    markdown: Optional[str] = None
    content: Optional[str] = None  # Alias for markdown for backward compatibility
    html: Optional[str] = None
    links: Optional[List[str]] = None
    metadata: Optional[Any] = None  # Use Any to allow our wrapper class

    model_config = {"arbitrary_types_allowed": True}

    def to_json(self) -> Dict[str, Any]:
        """Convert to JSON dict - consistent across all models"""
        data = self.model_dump()
        # Convert metadata wrapper to dict if present
        if self.metadata and hasattr(self.metadata, 'to_json'):
            data['metadata'] = self.metadata.to_json()
        return data
    
    @property 
    def text(self) -> Optional[str]:
        """Alias for markdown content"""
        return self.markdown or self.content
    
    @classmethod
    def from_scrape_response(cls, response):
        """Create from ScrapeResponse"""
        if response is None:
            return None
            
        from .scraper_client.types import UNSET
        
        # Extract content - could be in 'content' field
        content = getattr(response, "content", None)
        if content is UNSET:
            content = None
            
        # Extract HTML
        html = getattr(response, "html", None) 
        if html is UNSET:
            html = None
            
        # Extract links
        links = getattr(response, "links", None)
        if links is UNSET:
            links = None
            
        # Extract metadata
        metadata = PageMetadata.from_generated(getattr(response, "metadata", None))
        
        # For links format, if content is None but links exist, convert links to text content
        # This handles backward compatibility for the links format
        markdown_content = content
        if content is None and links and isinstance(links, list):
            # Convert links array to newline-separated text for backward compatibility
            markdown_content = '\n'.join(str(link) for link in links)
        elif content is None and links is not None and not isinstance(links, list):
            # If links is already a string, use it directly
            markdown_content = str(links)
        
        return cls(
            markdown=markdown_content,  # For backward compatibility
            content=content,   # For forward compatibility  
            html=html,
            links=links,
            metadata=metadata
        )
    
    @classmethod
    def from_page_content(cls, page_content):
        """Create from PageContent (for crawl results)"""
        if page_content is None:
            return None
            
        from .scraper_client.types import UNSET
        
        # Extract markdown
        markdown = getattr(page_content, "markdown", None)
        if markdown is UNSET:
            markdown = None
            
        # Extract HTML
        html = getattr(page_content, "html", None)
        if html is UNSET:
            html = None
            
        # Extract metadata
        metadata = PageMetadata.from_generated(getattr(page_content, "metadata", None))
        
        return cls(
            markdown=markdown,
            content=markdown,  # Alias
            html=html,
            links=None,  # PageContent doesn't have links
            metadata=metadata
        )


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

        # Build pages dict from crawl data using user-friendly Page wrappers
        pages: IndexableDict = IndexableDict()
        crawl_data = getattr(data, "crawl_data", None)
        if crawl_data is not None:
            crawl_props = getattr(crawl_data, "additional_properties", None)
            if isinstance(crawl_props, dict):
                # Convert PageContent objects to user-friendly Page objects
                for url, page_content in crawl_props.items():
                    page = Page.from_page_content(page_content)
                    if page:
                        pages[url] = page

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
    
    @property
    def is_completed(self) -> bool:
        """Check if the crawl job is completed"""
        return self.status and self.status.lower() == "completed"
    
    @property
    def is_failed(self) -> bool:
        """Check if the crawl job failed"""
        return self.status and self.status.lower() == "failed"
    
    @property
    def is_processing(self) -> bool:
        """Check if the crawl job is still processing"""
        return self.status and self.status.lower() in ("pending", "processing")

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
