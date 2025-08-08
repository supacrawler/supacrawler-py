from __future__ import annotations
import time
import httpx
from typing import Any, Dict, Optional
from .types import (
    ScrapeParams,
    ScrapeResponse,
    ScrapeLinksResponse,
    ScrapeContentResponse,
    JobCreateRequest,
    JobCreateResponse,
    JobStatusResponse,
    ScreenshotRequest,
    ScreenshotCreateResponse,
    WatchCreateRequest,
    WatchCreateResponse,
    WatchGetResponse,
    WatchListResponse,
    WatchDeleteResponse,
)

class SupacrawlerError(Exception):
    pass

class SupacrawlerClient:
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.supacrawler.com/api/v1",
        timeout_seconds: float = 30.0,
        client: Optional[httpx.Client] = None,
    ) -> None:
        self._api_key = api_key
        self._base_url = base_url.rstrip("/")
        self._timeout = timeout_seconds
        self._client = client or httpx.Client(timeout=timeout_seconds)

    def close(self) -> None:
        self._client.close()

    def _headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def _handle(self, resp: httpx.Response) -> Dict[str, Any]:
        if resp.status_code >= 400:
            try:
                payload = resp.json()
            except Exception:
                payload = {"error": resp.text}
            raise SupacrawlerError(f"HTTP {resp.status_code}: {payload}")
        return resp.json()

    # ------------- Scrape -------------
    def scrape(self, params: ScrapeParams) -> ScrapeResponse:
        query: Dict[str, Any] = {k: v for k, v in params.model_dump().items() if v is not None}
        url = f"{self._base_url}/scrape"
        resp = self._client.get(url, headers={"Authorization": f"Bearer {self._api_key}"}, params=query)
        data = self._handle(resp)
        if "links" in data:
            return ScrapeLinksResponse.model_construct(**data)
        else:
            return ScrapeContentResponse.model_construct(**data)

    # ------------- Jobs (crawl + status) -------------
    def create_job(self, request: JobCreateRequest) -> JobCreateResponse:
        url = f"{self._base_url}/jobs"
        resp = self._client.post(url, headers=self._headers(), json=request.model_dump(exclude_none=True))
        data = self._handle(resp)
        return JobCreateResponse.model_validate(data)

    def get_job(self, job_id: str) -> JobStatusResponse:
        url = f"{self._base_url}/jobs/{job_id}"
        resp = self._client.get(url, headers=self._headers())
        data = self._handle(resp)
        return JobStatusResponse.model_validate(data)

    def wait_for_job(self, job_id: str, interval_seconds: float = 3.0, timeout_seconds: float = 300.0) -> JobStatusResponse:
        start = time.time()
        while True:
            status = self.get_job(job_id)
            if status.status in ("completed", "failed"):
                return status
            if time.time() - start > timeout_seconds:
                raise SupacrawlerError(f"Timeout waiting for job {job_id}")
            time.sleep(interval_seconds)

    # ------------- Screenshots -------------
    def create_screenshot_job(self, request: ScreenshotRequest) -> ScreenshotCreateResponse:
        url = f"{self._base_url}/screenshots"
        resp = self._client.post(url, headers=self._headers(), json=request.model_dump(exclude_none=True))
        data = self._handle(resp)
        return ScreenshotCreateResponse.model_validate(data)

    # ------------- Watch -------------
    def watch_create(self, request: WatchCreateRequest) -> WatchCreateResponse:
        url = f"{self._base_url}/watch"
        resp = self._client.post(url, headers=self._headers(), json=request.model_dump(exclude_none=True))
        data = self._handle(resp)
        return WatchCreateResponse.model_validate(data)

    def watch_get(self, watch_id: str) -> WatchGetResponse:
        url = f"{self._base_url}/watch/{watch_id}"
        resp = self._client.get(url, headers=self._headers())
        data = self._handle(resp)
        return WatchGetResponse.model_validate(data)

    def watch_list(self) -> WatchListResponse:
        url = f"{self._base_url}/watch"
        resp = self._client.get(url, headers=self._headers())
        data = self._handle(resp)
        return WatchListResponse.model_validate(data)

    def watch_delete(self, watch_id: str) -> WatchDeleteResponse:
        url = f"{self._base_url}/watch/{watch_id}"
        resp = self._client.delete(url, headers=self._headers())
        data = self._handle(resp)
        return WatchDeleteResponse.model_validate(data)

    def watch_pause(self, watch_id: str) -> WatchDeleteResponse:
        url = f"{self._base_url}/watch/{watch_id}/pause"
        resp = self._client.patch(url, headers=self._headers())
        data = self._handle(resp)
        return WatchDeleteResponse.model_validate(data)

    def watch_resume(self, watch_id: str) -> WatchDeleteResponse:
        url = f"{self._base_url}/watch/{watch_id}/resume"
        resp = self._client.patch(url, headers=self._headers())
        data = self._handle(resp)
        return WatchDeleteResponse.model_validate(data)

    def watch_check(self, watch_id: str) -> WatchDeleteResponse:
        url = f"{self._base_url}/watch/{watch_id}/check"
        resp = self._client.post(url, headers=self._headers())
        data = self._handle(resp)
        return WatchDeleteResponse.model_validate(data)