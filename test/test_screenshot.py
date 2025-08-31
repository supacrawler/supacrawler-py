"""
Tests for screenshot endpoint functionality
"""

import pytest
from supacrawler import SupacrawlerClient
from supacrawler.scraper_client.models import ScreenshotCreateRequest


class TestScreenshotBasic:
    """Test basic screenshot functionality"""
    
    def test_create_screenshot_job(self, scraper_client, test_url):
        request = ScreenshotCreateRequest(
            url=test_url,
            format="png"
        )
        job = scraper_client.create_screenshot_job(request)
        assert hasattr(job, 'job_id')
        assert job.job_id is not None
        
    def test_screenshot_with_options(self, scraper_client, test_url):
        request = ScreenshotCreateRequest(
            url=test_url,
            format="png",
            full_page=True,
            width=1200,
            height=800
        )
        job = scraper_client.create_screenshot_job(request)
        assert hasattr(job, 'job_id')
        
    def test_get_screenshot_status(self, scraper_client, test_url):
        request = ScreenshotCreateRequest(
            url=test_url,
            format="jpeg"
        )
        job = scraper_client.create_screenshot_job(request)
        status = scraper_client.get_screenshot(job.job_id)
        assert hasattr(status, 'status')


class TestScreenshotBackend:
    """Test screenshot via backend (requires API key)"""
    
    def test_backend_screenshot_basic(self, backend_client, test_url):
        request = ScreenshotCreateRequest(
            url=test_url,
            format="png"
        )
        job = backend_client.create_screenshot_job(request)
        assert hasattr(job, 'job_id')
        
    def test_backend_screenshot_status(self, backend_client, test_url):
        request = ScreenshotCreateRequest(
            url=test_url,
            format="png"
        )
        job = backend_client.create_screenshot_job(request)
        status = backend_client.get_screenshot(job.job_id)
        assert hasattr(status, 'status')

    def test_format_variations(self, scraper_client, test_url):
        """Test different format strings are accepted"""
        # Test lowercase png
        request = ScreenshotCreateRequest(url=test_url, format="png")
        job = scraper_client.create_screenshot_job(request)
        assert hasattr(job, 'job_id')
        
        # Test uppercase PNG
        request = ScreenshotCreateRequest(url=test_url, format="PNG")
        job = scraper_client.create_screenshot_job(request)
        assert hasattr(job, 'job_id')
        
        # Test jpeg
        request = ScreenshotCreateRequest(url=test_url, format="jpeg")
        job = scraper_client.create_screenshot_job(request)
        assert hasattr(job, 'job_id')
        
        # Test jpg (should convert to jpeg)
        request = ScreenshotCreateRequest(url=test_url, format="jpg")
        job = scraper_client.create_screenshot_job(request)
        assert hasattr(job, 'job_id')

    def test_invalid_format_error(self, scraper_client, test_url):
        """Test that invalid formats raise ValueError"""
        with pytest.raises(ValueError, match="Unsupported format.*gif.*Supported formats are: png, jpeg, jpg"):
            request = ScreenshotCreateRequest(url=test_url, format="gif")
            request.to_dict()  # This should trigger the validation
