from __future__ import annotations
from typing import Dict, List, Optional, Union, Literal
from pydantic import BaseModel, Field

# ------------ Scrape ------------

ScrapeFormat = Literal["markdown", "html", "text", "links"]
DeviceType = Literal["desktop", "mobile"]

class ScrapeParams(BaseModel):
    url: str
    format: ScrapeFormat = "markdown"
    render_js: Optional[bool] = False
    wait: Optional[int] = None
    device: Optional[DeviceType] = None
    depth: Optional[int] = None
    max_links: Optional[int] = None
    fresh: Optional[bool] = None

class ScrapeContentMetadata(BaseModel):
    status_code: int

class ScrapeLinksMetadata(BaseModel):
    status_code: int
    depth: Optional[int] = None

class ScrapeContentResponse(BaseModel):
    success: bool
    url: str
    content: str
    title: Optional[str] = None
    metadata: ScrapeContentMetadata

class ScrapeLinksResponse(BaseModel):
    success: bool
    url: str
    links: List[str]
    discovered: int
    metadata: ScrapeLinksMetadata

ScrapeResponse = Union[ScrapeContentResponse, ScrapeLinksResponse]

# ------------ Jobs (crawl + status) ------------

JobType = Literal["crawl", "screenshot"]
JobStatus = Literal["processing", "completed", "failed", "not_found", "expired"]

class JobCreateRequest(BaseModel):
    url: str
    type: Literal["crawl"]
    format: Optional[Literal["markdown", "html", "text"]] = None
    link_limit: Optional[int] = None
    depth: Optional[int] = None
    include_subdomains: Optional[bool] = None
    render_js: Optional[bool] = None
    patterns: Optional[List[str]] = None

class JobCreateResponse(BaseModel):
    success: bool
    job_id: str
    type: Literal["crawl"]
    status: Literal["processing"]
    status_url: str

class PageMetadata(BaseModel):
    title: Optional[str] = None
    status_code: Optional[int] = None

class PageData(BaseModel):
    markdown: Optional[str] = None
    html: Optional[str] = None
    metadata: Optional[PageMetadata] = None

class CrawlStatistics(BaseModel):
    total_pages: Optional[int] = None
    successful_pages: Optional[int] = None
    failed_pages: Optional[int] = None

class JobDataCrawl(BaseModel):
    url: str
    crawl_data: Dict[str, PageData] = Field(default_factory=dict)
    error_data: Dict[str, str] = Field(default_factory=dict)
    statistics: Optional[CrawlStatistics] = None
    render_js: Optional[bool] = None

class ScreenshotMetadata(BaseModel):
    device: Optional[str] = None
    format: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    file_size: Optional[int] = None
    load_time: Optional[int] = None
    quality: Optional[int] = None
    device_scale: Optional[float] = None

class JobDataScreenshot(BaseModel):
    url: str
    screenshot: str
    metadata: Optional[ScreenshotMetadata] = None

JobData = Union[JobDataCrawl, JobDataScreenshot]

class JobStatusResponse(BaseModel):
    job_id: str
    type: JobType
    status: JobStatus
    data: Optional[JobData] = None

# ------------ Screenshots ------------

class ScreenshotRequest(BaseModel):
    url: str
    device: Optional[str] = None
    full_page: Optional[bool] = None
    format: Optional[Literal["png", "jpeg", "webp"]] = None
    quality: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    device_scale: Optional[float] = None
    is_mobile: Optional[bool] = None
    has_touch: Optional[bool] = None
    is_landscape: Optional[bool] = None
    delay: Optional[int] = None
    timeout: Optional[int] = None
    wait_for_selector: Optional[str] = None
    wait_until: Optional[Literal["load", "domcontentloaded", "networkidle"]] = None
    scroll_delay: Optional[int] = None
    click_selector: Optional[str] = None
    hide_selectors: Optional[List[str]] = None
    block_ads: Optional[bool] = None
    block_cookies: Optional[bool] = None
    block_chats: Optional[bool] = None
    block_trackers: Optional[bool] = None
    block_resources: Optional[List[Literal["image", "stylesheet", "script", "font"]]] = None
    user_agent: Optional[str] = None
    headers: Optional[Dict[str, str]] = None
    cookies: Optional[List[Dict[str, Union[str, int, bool]]]] = None
    dark_mode: Optional[bool] = None
    reduced_motion: Optional[bool] = None
    high_contrast: Optional[bool] = None
    disable_js: Optional[bool] = None
    print_mode: Optional[bool] = None
    ignore_https: Optional[bool] = None

class ScreenshotCreateResponse(BaseModel):
    success: bool
    job_id: str
    type: Literal["screenshot"]
    status: Literal["processing"]
    status_url: str
    url: Optional[str] = None
    screenshot: Optional[str] = None
    metadata: Optional[ScreenshotMetadata] = None

# ------------ Watch ------------

Frequency = Literal["hourly", "daily", "weekly", "monthly", "custom"]

class WatchCreateRequest(BaseModel):
    url: str
    frequency: Frequency
    notify_email: Optional[str] = None
    selector: Optional[str] = None
    include_html: Optional[bool] = None
    include_image: Optional[bool] = None
    full_page: Optional[bool] = None
    quality: Optional[int] = None
    custom_frequency: Optional[str] = None

class WatchCreateResponse(BaseModel):
    success: bool
    watch_id: str
    message: Optional[str] = None

class Watch(BaseModel):
    id: Optional[str] = None
    user_id: Optional[str] = None
    url: Optional[str] = None
    frequency: Optional[str] = None
    notify_email: Optional[str] = None
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

class WatchResult(BaseModel):
    id: Optional[str] = None
    executed_at: Optional[str] = None
    has_changed: Optional[bool] = None
    change_type: Optional[str] = None
    content_hash: Optional[str] = None
    content: Optional[str] = None
    html_content: Optional[str] = None
    image_url: Optional[str] = None

class WatchGetResponse(BaseModel):
    success: bool
    watch: Optional[Watch] = None
    results: Optional[List[WatchResult]] = None

class WatchListResponse(BaseModel):
    success: bool
    total: Optional[int] = None
    watches: List[Watch] = Field(default_factory=list)

class WatchDeleteResponse(BaseModel):
    success: bool
    message: Optional[str] = None