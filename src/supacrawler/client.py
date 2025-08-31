from __future__ import annotations

import time
from typing import Any, Dict, Optional, Union

import httpx

from .scraper_client.api.jobs.get_v_1_crawl_job_id import sync as crawl_get_sync
from .scraper_client.api.jobs.post_v1_crawl import sync as crawl_create_sync
from .scraper_client.api.scrape.get_v1_scrape import (
    sync as scrape_sync,
)
from .scraper_client.api.screenshots.get_v1_screenshots import sync as screenshots_get_sync
from .scraper_client.api.screenshots.post_v1_screenshots import sync as screenshots_create_sync

# Generated engine client (created by Makefile gen-openapi under supacrawler_scraper_engine_api_client)
from .scraper_client.client import Client as EngineClient
from .scraper_client.errors import UnexpectedStatus
from .scraper_client.models import (
    CrawlCreateRequest,
    CrawlCreateRequestFormat,
    CrawlCreateResponse,
    GetV1ScrapeFormat,
    ScreenshotCreateRequest,
)
from .types import (
    CrawlJob,
    ScreenshotJob,
    WatchCreateRequest,
    WatchCreateResponse,
    WatchDeleteResponse,
    WatchGetResponse,
    WatchListResponse,
)


class SupacrawlerError(Exception):
    """Base exception for Supacrawler API errors"""

    def __init__(self, message: str, status_code: Optional[int] = None, error_type: Optional[str] = None):
        super().__init__(message)
        self.status_code = status_code
        self.error_type = error_type


class SupacrawlerBadRequestError(SupacrawlerError):
    """HTTP 400 - Bad Request"""

    pass


class SupacrawlerForbiddenError(SupacrawlerError):
    """HTTP 403 - Forbidden (e.g., robots.txt disallowed)"""

    pass


class SupacrawlerNotFoundError(SupacrawlerError):
    """HTTP 404 - Not Found"""

    pass


class SupacrawlerTimeoutError(SupacrawlerError):
    """HTTP 408 - Request Timeout"""

    pass


class SupacrawlerUnprocessableError(SupacrawlerError):
    """HTTP 422 - Unprocessable Entity (content filtered)"""

    pass


class SupacrawlerRateLimitError(SupacrawlerError):
    """HTTP 429 - Too Many Requests"""

    pass


class SupacrawlerServerError(SupacrawlerError):
    """HTTP 5xx - Server Error"""

    pass


class SupacrawlerClient:
    def __init__(
        self,
        api_key: str,
        base_url: Optional[str] = None,
        timeout_seconds: float = 30.0,
        client: Optional[httpx.Client] = None,
    ) -> None:
        self._api_key = api_key or ""
        # Auto-select base when not provided: hosted if API key, else local engine
        if base_url is None or not str(base_url).strip():
            base_url = "https://api.supacrawler.com/api" if self._api_key else "http://localhost:8081"
        self._base_url = base_url.rstrip("/")
        self._timeout = timeout_seconds
        self._client = client or httpx.Client(timeout=timeout_seconds)
        # Engine client uses /api as base; endpoints add /v1/
        self._engine = EngineClient(base_url=f"{self._base_url}", headers=self._headers(), timeout=timeout_seconds)

    def close(self) -> None:
        self._client.close()

    def _headers(self) -> Dict[str, str]:
        headers: Dict[str, str] = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        if self._api_key:
            headers["Authorization"] = f"Bearer {self._api_key}"
        return headers

    def _handle(self, resp: httpx.Response) -> Dict[str, Any]:
        if resp.status_code >= 400:
            try:
                payload = resp.json()
                error_msg = payload.get("error", resp.text) if isinstance(payload, dict) else str(payload)
            except Exception:
                error_msg = resp.text
                payload = {"error": error_msg}

            # Map status codes to specific exception types
            if resp.status_code == 400:
                raise SupacrawlerBadRequestError(error_msg, resp.status_code, "bad_request")
            elif resp.status_code == 403:
                raise SupacrawlerForbiddenError(error_msg, resp.status_code, "forbidden")
            elif resp.status_code == 404:
                raise SupacrawlerNotFoundError(error_msg, resp.status_code, "not_found")
            elif resp.status_code == 408:
                raise SupacrawlerTimeoutError(error_msg, resp.status_code, "timeout")
            elif resp.status_code == 422:
                raise SupacrawlerUnprocessableError(error_msg, resp.status_code, "unprocessable")
            elif resp.status_code == 429:
                raise SupacrawlerRateLimitError(error_msg, resp.status_code, "rate_limit")
            elif resp.status_code >= 500:
                raise SupacrawlerServerError(error_msg, resp.status_code, "server_error")
            else:
                raise SupacrawlerError(f"HTTP {resp.status_code}: {error_msg}", resp.status_code)
        return resp.json()

    # ------------- Scrape (via engine client) -------------
    def scrape(self, url: str, **kwargs):
        """Scrape a single URL (engine /v1/scrape)

        Accepts kwargs: format (str or GetV1ScrapeFormat), depth, max_links, render_js, include_html, fresh

        Raises:
            SupacrawlerBadRequestError: Invalid URL or parameters (HTTP 400)
            SupacrawlerForbiddenError: Robots.txt disallowed (HTTP 403)
            SupacrawlerNotFoundError: Page not found (HTTP 404)
            SupacrawlerTimeoutError: Request timeout (HTTP 408)
            SupacrawlerUnprocessableError: Content filtered or invalid (HTTP 422)
            SupacrawlerRateLimitError: Rate limited (HTTP 429)
            SupacrawlerServerError: Engine error (HTTP 5xx)
        """
        fmt = kwargs.pop("format", None)
        format_: Optional[GetV1ScrapeFormat] = None
        if isinstance(fmt, GetV1ScrapeFormat):
            format_ = fmt
        elif isinstance(fmt, str):
            fmt_norm = fmt.strip().lower()
            if fmt_norm in ("markdown", "links"):
                format_ = GetV1ScrapeFormat(fmt_norm)

        try:
            # Handle format properly - use UNSET if not provided
            from .scraper_client.types import UNSET

            if format_ is None:
                format_ = UNSET

            # Pass url as url_query to generated client
            resp = scrape_sync(
                client=self._engine,
                url_query=url,
                format_=format_,
                depth=kwargs.get("depth"),
                max_links=kwargs.get("max_links"),
                render_js=kwargs.get("render_js"),
                include_html=kwargs.get("include_html"),
                fresh=kwargs.get("fresh"),
            )
            if resp is None or isinstance(resp, dict) and resp.get("error"):
                raise SupacrawlerError(f"Scrape failed for {url}")

            # Convert to friendly Page object
            from .scraper_client.types import UNSET
            from .types import Page, PageMetadata

            if hasattr(resp, "content"):
                # Extract metadata if available
                page_metadata = None
                raw_metadata = getattr(resp, "metadata", None)
                if raw_metadata is not None:
                    metadata_dict = {}
                    # Handle scrape metadata structure
                    for field in ["title", "status_code", "description", "language"]:
                        value = getattr(raw_metadata, field, None)
                        if value is not None and value is not UNSET:
                            metadata_dict[field] = value
                    # Add title from top-level if not in metadata
                    if "title" not in metadata_dict:
                        title = getattr(resp, "title", None)
                        if title is not None and title is not UNSET:
                            metadata_dict["title"] = title
                    if metadata_dict:
                        page_metadata = PageMetadata(**metadata_dict)

                # Handle different response formats
                markdown_content = None
                links_data = getattr(resp, "links", None)
                
                # Check what format was requested
                if format_ and str(format_).lower() == "links":
                    # For links format, extract links array directly
                    if links_data and links_data is not UNSET:
                        if isinstance(links_data, list):
                            links_list = links_data
                        else:
                            links_list = None
                    else:
                        links_list = None
                    markdown_content = None  # No markdown for links format
                else:
                    # For markdown/text format, extract from content field
                    markdown_content = getattr(resp, "content", "")
                    if markdown_content is UNSET:
                        markdown_content = ""
                    links_list = None  # No links for markdown format
                
                # Get HTML content if include_html was requested
                html_content = getattr(resp, "html", None)
                if html_content is UNSET:
                    html_content = None

                return Page(
                    markdown=markdown_content,
                    html=html_content,
                    links=links_list,
                    metadata=page_metadata,
                )

            return resp
        except UnexpectedStatus as e:
            # Convert UnexpectedStatus to our specific error types
            error_msg = e.content.decode("utf-8", errors="ignore")
            try:
                import json

                error_data = json.loads(error_msg)
                if isinstance(error_data, dict) and "error" in error_data:
                    error_msg = error_data["error"]
            except (json.JSONDecodeError, TypeError):
                pass

            # Map status codes to specific exception types
            if e.status_code == 400:
                raise SupacrawlerBadRequestError(error_msg, e.status_code, "bad_request") from e
            elif e.status_code == 403:
                raise SupacrawlerForbiddenError(error_msg, e.status_code, "forbidden") from e
            elif e.status_code == 404:
                raise SupacrawlerNotFoundError(error_msg, e.status_code, "not_found") from e
            elif e.status_code == 408:
                raise SupacrawlerTimeoutError(error_msg, e.status_code, "timeout") from e
            elif e.status_code == 422:
                raise SupacrawlerUnprocessableError(error_msg, e.status_code, "unprocessable") from e
            elif e.status_code == 429:
                raise SupacrawlerRateLimitError(error_msg, e.status_code, "rate_limit") from e
            elif e.status_code >= 500:
                raise SupacrawlerServerError(error_msg, e.status_code, "server_error") from e
            else:
                raise SupacrawlerError(f"Scrape failed for {url}: {error_msg}", e.status_code) from e

    # ------------- Crawl (via engine client) -------------
    def create_crawl_job(
        self, request: Optional[Union[CrawlCreateRequest, Dict[str, Any]]] = None, **kwargs
    ) -> CrawlCreateResponse:
        """Create a crawl job (engine /v1/crawl)

        Usage:
            - create_crawl_job(url="https://...", format="markdown", depth=2, link_limit=5, include_subdomains=False, render_js=False)
            - create_crawl_job({"url": "https://...", "format": "markdown", ...})
            - create_crawl_job(CrawlCreateRequest(...))
        """
        # Merge kwargs into request dict if provided that way
        if request is None and kwargs:
            request = dict(kwargs)

        if isinstance(request, dict):
            req_dict = dict(request)
            # Normalize format (string -> enum)
            if "format" in req_dict and "format_" not in req_dict:
                fmt = req_dict.pop("format")
                if isinstance(fmt, CrawlCreateRequestFormat):
                    req_dict["format_"] = fmt
                elif isinstance(fmt, str):
                    fmt_norm = fmt.strip().lower()
                    if fmt_norm in ("markdown", "html"):
                        req_dict["format_"] = CrawlCreateRequestFormat(fmt_norm)
            # Build model from normalized dict
            from .scraper_client.types import UNSET

            # Handle format properly - use UNSET if not provided
            format_val = req_dict.get("format_")
            if format_val is None:
                format_val = UNSET

            model = CrawlCreateRequest(
                url=req_dict["url"],
                format_=format_val,
                depth=req_dict.get("depth"),
                link_limit=req_dict.get("link_limit"),
                include_subdomains=req_dict.get("include_subdomains"),
                render_js=req_dict.get("render_js"),
                include_html=req_dict.get("include_html"),
            )
            r = crawl_create_sync(client=self._engine, body=model)
            if r is None:
                raise SupacrawlerError("No response from server - check if scraper engine is running")
            
            # Handle Error responses (400, 429, etc.)
            if hasattr(r, "error") and hasattr(r, "success"):
                error_msg = getattr(r, "error", "Unknown error")
                raise SupacrawlerError(f"Crawl job creation failed: {error_msg}")
            
            # Handle successful CrawlCreateResponse
            if hasattr(r, "success") and getattr(r, "success") is False:
                error_msg = getattr(r, "error", "Failed to create crawl job")
                raise SupacrawlerError(f"Crawl job creation failed: {error_msg}")
            return r

        if isinstance(request, CrawlCreateRequest):
            r = crawl_create_sync(client=self._engine, body=request)
            if r is None:
                raise SupacrawlerError("No response from server - check if scraper engine is running")
            
            # Handle Error responses (400, 429, etc.)
            if hasattr(r, "error") and hasattr(r, "success"):
                error_msg = getattr(r, "error", "Unknown error")
                raise SupacrawlerError(f"Crawl job creation failed: {error_msg}")
            
            # Handle successful CrawlCreateResponse
            if hasattr(r, "success") and getattr(r, "success") is False:
                error_msg = getattr(r, "error", "Failed to create crawl job")
                raise SupacrawlerError(f"Crawl job creation failed: {error_msg}")
            return r

        raise SupacrawlerError("create_crawl_job requires either kwargs, dict, or CrawlCreateRequest model")

    def get_crawl(self, job_id: str) -> CrawlJob:
        resp = crawl_get_sync(client=self._engine, job_id=job_id)
        return CrawlJob.from_engine(resp)

    def wait_for_crawl(self, job_id: str, interval_seconds: float = 3.0, timeout_seconds: float = 600.0) -> CrawlJob:
        start = time.time()
        while True:
            job: CrawlJob = self.get_crawl(job_id)
            status = (job.status or "").lower()
            if status in ("completed", "failed"):
                return job
            if time.time() - start > timeout_seconds:
                raise SupacrawlerError(f"Timeout waiting for crawl {job_id}")
            time.sleep(interval_seconds)

    # ------------- Screenshots (via engine client) -------------
    def create_screenshot_job(self, request: ScreenshotCreateRequest) -> ScreenshotJob:
        resp = screenshots_create_sync(client=self._engine, body=request)
        return ScreenshotJob.from_engine(resp)

    def get_screenshot(self, job_id: str) -> ScreenshotJob:
        resp = screenshots_get_sync(client=self._engine, job_id=job_id)
        return ScreenshotJob.from_engine(resp)

    def wait_for_screenshot(
        self, job_id: str, interval_seconds: float = 3.0, timeout_seconds: float = 300.0
    ) -> ScreenshotJob:
        start = time.time()
        while True:
            resp = self.get_screenshot(job_id)
            status = resp.status or ""
            if status.lower() == "completed":
                return resp
            if time.time() - start > timeout_seconds:
                raise SupacrawlerError(f"Timeout waiting for screenshot {job_id}")
            time.sleep(interval_seconds)

    # ------------- Watch (backend) -------------
    def watch_create(self, request: WatchCreateRequest) -> WatchCreateResponse:
        url = f"{self._base_url}/v1/watch"
        resp = self._client.post(url, headers=self._headers(), json=request.model_dump(exclude_none=True))
        data = self._handle(resp)
        return WatchCreateResponse.model_validate(data)

    def watch_get(self, watch_id: str) -> WatchGetResponse:
        url = f"{self._base_url}/v1/watch/{watch_id}"
        resp = self._client.get(url, headers=self._headers())
        data = self._handle(resp)
        return WatchGetResponse.model_validate(data)

    def watch_list(self) -> WatchListResponse:
        url = f"{self._base_url}/v1/watch"
        resp = self._client.get(url, headers=self._headers())
        data = self._handle(resp)
        return WatchListResponse.model_validate(data)

    def watch_delete(self, watch_id: str) -> WatchDeleteResponse:
        url = f"{self._base_url}/v1/watch/{watch_id}"
        resp = self._client.delete(url, headers=self._headers())
        data = self._handle(resp)
        return WatchDeleteResponse.model_validate(data)

    def watch_pause(self, watch_id: str) -> WatchDeleteResponse:
        url = f"{self._base_url}/v1/watch/{watch_id}/pause"
        resp = self._client.patch(url, headers=self._headers())
        data = self._handle(resp)
        return WatchDeleteResponse.model_validate(data)

    def watch_resume(self, watch_id: str) -> WatchDeleteResponse:
        url = f"{self._base_url}/v1/watch/{watch_id}/resume"
        resp = self._client.patch(url, headers=self._headers())
        data = self._handle(resp)
        return WatchDeleteResponse.model_validate(data)

    def watch_check(self, watch_id: str) -> WatchDeleteResponse:
        url = f"{self._base_url}/v1/watch/{watch_id}/check"
        resp = self._client.post(url, headers=self._headers())
        data = self._handle(resp)
        return WatchDeleteResponse.model_validate(data)
