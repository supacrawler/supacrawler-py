"""
Tests for data model functionality (to_json, IndexableDict, etc.)
"""

import pytest
from supacrawler import SupacrawlerClient


class TestDataModels:
    """Test custom data model functionality"""
    
    def test_page_to_json(self, scraper_client, test_url):
        result = scraper_client.scrape(test_url, format='markdown')
        assert hasattr(result, 'to_json')
        json_data = result.to_json()
        assert isinstance(json_data, dict)
        assert 'markdown' in json_data
        
    def test_metadata_to_json(self, scraper_client, test_url):
        result = scraper_client.scrape(test_url, format='markdown')
        if result.metadata:
            assert hasattr(result.metadata, 'to_json')
            json_data = result.metadata.to_json()
            assert isinstance(json_data, dict)
            
    def test_screenshot_to_json(self, scraper_client, test_url):
        from supacrawler.scraper_client.models import ScreenshotCreateRequest, ScreenshotCreateRequestFormat
        
        request = ScreenshotCreateRequest(
            url=test_url,
            format_=ScreenshotCreateRequestFormat.PNG
        )
        job = scraper_client.create_screenshot_job(request)
        assert hasattr(job, 'to_json')
        json_data = job.to_json()
        assert isinstance(json_data, dict)


class TestIndexableDict:
    """Test IndexableDict functionality for crawl data"""
    
    def test_crawl_indexable_dict(self, scraper_client, test_url):
        # Create a crawl and wait a bit for some data
        job = scraper_client.create_crawl_job(url=test_url, depth=1, link_limit=2)
        
        # Get status (may have data)
        status = scraper_client.get_crawl(job.job_id)
        
        if status.data and status.data.pages:
            # Test IndexableDict functionality
            pages = status.data.pages
            
            # Test len() works
            assert len(pages) >= 0
            
            # Test dict access works
            if len(pages) > 0:
                first_key = list(pages.keys())[0]
                assert first_key in pages
                
                # Test index access works
                assert pages[0] is not None
                assert pages.first() is not None
                
                # Test get_key works
                assert pages.get_key(0) == first_key
