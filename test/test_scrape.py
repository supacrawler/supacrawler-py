"""
Tests for scrape endpoint functionality
"""

import pytest
from supacrawler import SupacrawlerClient


class TestScrapeFormats:
    """Test different scrape formats"""
    
    def test_markdown_format(self, scraper_client, test_url):
        result = scraper_client.scrape(test_url, format='markdown')
        assert result.markdown is not None
        assert len(result.markdown) > 0
        
    def test_links_format(self, scraper_client, test_url):
        result = scraper_client.scrape(test_url, format='links')
        # For links format, we should get a list of links, not markdown
        assert result.links is not None
        assert isinstance(result.links, list)
        assert len(result.links) > 0
        # Verify each item is a string (URL)
        for link in result.links:
            assert isinstance(link, str)
            assert link.startswith('http')
        # For links format, markdown should be None
        assert result.markdown is None
        
    def test_include_html(self, scraper_client, test_url):
        result = scraper_client.scrape(test_url, format='markdown', include_html=True)
        assert result.markdown is not None
        assert result.html is not None
        assert len(result.html) > 0


class TestScrapeParameters:
    """Test scrape parameters"""
    
    def test_fresh_parameter(self, scraper_client, test_url):
        result = scraper_client.scrape(test_url, fresh=True)
        assert result.markdown is not None
        
    def test_combined_parameters(self, scraper_client, test_url):
        result = scraper_client.scrape(
            test_url,
            format='markdown',
            include_html=True,
            fresh=True,
            depth=1,
            max_links=5
        )
        assert result.markdown is not None
        assert result.html is not None


class TestScrapeLinksFormat:
    """Test comprehensive links format behavior"""
    
    def test_links_format_structure(self, scraper_client, test_url):
        """Test that links format returns proper structure"""
        result = scraper_client.scrape(test_url, format='links')
        
        # Should have links array
        assert result.links is not None
        assert isinstance(result.links, list)
        assert len(result.links) > 0
        
        # Should NOT have markdown content
        assert result.markdown is None
        
        # HTML should be None unless explicitly requested
        assert result.html is None
        
    def test_links_format_with_html(self, scraper_client, test_url):
        """Test links format with HTML inclusion"""
        result = scraper_client.scrape(test_url, format='links', include_html=True)
        
        # Should have links array
        assert result.links is not None
        assert isinstance(result.links, list)
        
        # Should have HTML content when requested
        assert result.html is not None
        assert len(result.html) > 0
        
        # Should NOT have markdown content
        assert result.markdown is None
        
    def test_links_vs_markdown_format(self, scraper_client, test_url):
        """Test difference between links and markdown format"""
        links_result = scraper_client.scrape(test_url, format='links')
        markdown_result = scraper_client.scrape(test_url, format='markdown')
        
        # Links format should have links array, no markdown
        assert links_result.links is not None
        assert isinstance(links_result.links, list)
        assert links_result.markdown is None
        
        # Markdown format should have markdown content, no links
        assert markdown_result.markdown is not None
        assert isinstance(markdown_result.markdown, str)
        assert markdown_result.links is None


class TestScrapeBackend:
    """Test scrape via backend (requires API key)"""
    
    def test_backend_scrape_basic(self, backend_client, test_url):
        result = backend_client.scrape(test_url, format='markdown')
        assert result.markdown is not None
        
    def test_backend_scrape_with_html(self, backend_client, test_url):
        result = backend_client.scrape(test_url, format='markdown', include_html=True)
        assert result.markdown is not None
        assert result.html is not None
        
    def test_backend_scrape_links_format(self, backend_client, test_url):
        """Test backend links format"""
        result = backend_client.scrape(test_url, format='links')
        assert result.links is not None
        assert isinstance(result.links, list)
        assert result.markdown is None
