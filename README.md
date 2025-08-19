# supacrawler-py

Typed Python SDK for Supacrawler API.

## Install

- From PyPI (when published):
```bash
pip install supacrawler-py
```

- With uv (PEP 621 aware):
```bash
uv add supacrawler-py
# or for local dev
uv pip install -e .
```

- From local path (development):
```bash
pip install -e .
```

- From GitHub (direct):
```bash
pip install git+https://github.com/Supacrawler/supacrawler-py.git#subdirectory=sdk/supacrawler-py
```

## Usage

```python
from supacrawler import SupacrawlerClient, ScrapeParams, JobCreateRequest, ScreenshotRequest, WatchCreateRequest

client = SupacrawlerClient(api_key="YOUR_API_KEY")

# Scrape
scrape = client.scrape(ScrapeParams(url="https://example.com", format="markdown"))
print(scrape)

# Create crawl job
job = client.create_job(JobCreateRequest(url="https://supabase.com/docs", type="crawl", depth=2, link_limit=10, format="markdown"))
status = client.wait_for_job(job.job_id)
print(status.status)

# Screenshot job
sjob = client.create_screenshot_job(ScreenshotRequest(url="https://example.com", device="desktop", full_page=True))
print("job:", sjob.job_id)

# Wait and fetch a fresh signed URL (recommended)
signed = client.wait_for_screenshot(sjob.job_id)
print("screenshot:", signed.screenshot)

# Watch
watch = client.watch_create(WatchCreateRequest(url="https://example.com/pricing", frequency="daily", notify_email="me@example.com"))
print(watch.watch_id)
```

### Advanced
- See [`examples/*.ipynb`](https://github.com/Supacrawler/supacrawler-py/tree/main/examples) for full parameter coverage:
  - Scrape: format, render_js, wait, device, depth, max_links, fresh
  - Jobs: format, link_limit, depth, include_subdomains, render_js, patterns
  - Screenshots: device/full_page/format/quality/viewport/device_scale, waits, selectors, blocking, modes
  - Watch: frequency, selector, include_html/image, full_page, quality, pause/resume/check/delete

## API coverage
- GET `/v1/scrape` (all params)
- POST `/v1/crawl`, GET `/v1/crawl/{id}`
- POST `/v1/screenshots`
- POST `/v1/watch`, GET `/v1/watch`, GET `/v1/watch/{id}`, DELETE `/v1/watch/{id}`, PATCH `/v1/watch/{id}/pause`, PATCH `/v1/watch/{id}/resume`, POST `/v1/watch/{id}/check`

## Development
- Env var: `SUPACRAWLER_API_KEY` for examples.
- Not needed: `requirements.txt` for end-users (deps declared in `pyproject.toml`). Optional `requirements-dev.txt` if you add tests or notebooks tooling.