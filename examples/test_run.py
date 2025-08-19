import os
import time
from supacrawler import SupacrawlerClient


def main():
    api_key = os.environ.get("SUPACRAWLER_API_KEY", "")
    base_url = os.environ.get("SUPACRAWLER_BASE_URL")
    if not base_url:
        # If no API key, default to local engine (no auth). Otherwise use hosted API
        base_url = "http://localhost:8081" if not api_key else "https://api.supacrawler.com/api"
    client = SupacrawlerClient(api_key=api_key, base_url=base_url)

    # Simple scrape (string format ok)
    r = client.scrape("https://example.com", format="markdown")
    if r is None:
        raise RuntimeError("Scrape failed (None). Ensure SUPACRAWLER_BASE_URL points to engine or set SUPACRAWLER_API_KEY for hosted API.")
    print("Scrape OK, url=", getattr(r, "url", None))

    # Create crawl with simple kwargs (no enums required)
    job = client.create_crawl_job(
        url="https://supabase.com/docs",
        format="markdown",
        link_limit=3,
        depth=1,
        include_subdomains=False,
        render_js=False,
    )
    print("Crawl job id:", job.job_id)

    # Poll until done
    start = time.time()
    while True:
        status = client.get_crawl(job.job_id)
        s = str(getattr(status, "status", "")).lower()
        print("status:", s)
        if s in ("completed", "failed"):
            break
        if time.time() - start > 120:
            raise RuntimeError("Timeout waiting for crawl")
        time.sleep(2)

    print("Final:", status.status)
    if status.data and status.data.crawl_data:
        # crawl_data is a typed mapping wrapper with .to_dict()
        try:
            crawl_map = status.data.crawl_data.to_dict()  # generated helper
        except Exception:
            crawl_map = dict(getattr(status.data.crawl_data, "additional_properties", {}))
        print("Pages:", len(crawl_map))


if __name__ == "__main__":
    main()


