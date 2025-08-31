"""
Tests for crawl endpoint functionality
"""

import pytest
from supacrawler import SupacrawlerClient


class TestCrawlBasic:
    """Test basic crawl functionality"""
    
    def test_create_crawl_job(self, scraper_client, test_url):
        job = scraper_client.create_crawl_job(url=test_url, depth=1)
        assert hasattr(job, 'job_id')
        assert job.job_id is not None
        
    def test_get_crawl_status(self, scraper_client, test_url):
        job = scraper_client.create_crawl_job(url=test_url, depth=1)
        status = scraper_client.get_crawl(job.job_id)
        assert hasattr(status, 'status')
        
    def test_crawl_with_parameters(self, scraper_client, test_url):
        job = scraper_client.create_crawl_job(
            url=test_url,
            depth=2,
            format="markdown",
            include_html=True,
            link_limit=5
        )
        assert hasattr(job, 'job_id')


class TestCrawlBackend:
    """Test crawl via backend (requires API key)"""
    
    def test_backend_crawl_basic(self, backend_client, test_url):
        job = backend_client.create_crawl_job(url=test_url, depth=1, format="markdown")
        assert hasattr(job, 'job_id')
        
    def test_backend_crawl_status(self, backend_client, test_url):
        job = backend_client.create_crawl_job(url=test_url, depth=1, format="markdown")
        status = backend_client.get_crawl(job.job_id)
        assert hasattr(status, 'status')
