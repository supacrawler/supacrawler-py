from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field

# Keep only watch-related types here. Engine API types are generated under engine_client.

# ------------ Watch ------------


class WatchCreateRequest(BaseModel):
    url: str
    frequency: str
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
