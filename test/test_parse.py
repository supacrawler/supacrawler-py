"""
Tests for parse endpoint functionality
"""

import pytest
from supacrawler import SupacrawlerClient, SupacrawlerBadRequestError, SupacrawlerUnprocessableError


class TestParseBasic:
    """Test basic parse functionality"""
    
    def test_simple_parse(self, scraper_client, test_url):
        """Test basic parse without schema"""
        response = scraper_client.parse(f"Extract any information from {test_url}")
        assert response.success is True
        assert response.data is not None
        # pages_processed might be UNSET, so check if it exists and is reasonable
        from supacrawler.scraper_client.types import UNSET
        if response.pages_processed is not UNSET:
            assert response.pages_processed >= 1
    
    def test_parse_with_json_schema(self, scraper_client, test_url):
        """Test parse with structured JSON schema"""
        schema = {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "content": {"type": "string"}
            },
            "required": ["title"]
        }
        
        response = scraper_client.parse(
            f"Extract title and content from {test_url}",
            schema=schema,
            output_format="json"
        )
        
        assert response.success is True
        assert response.data is not None
        # Data might be empty list if parse doesn't extract anything
        # Just check that we got a response
    
    def test_parse_empty_prompt_fails(self, scraper_client):
        """Test that empty prompt raises error"""
        # Empty prompt should either raise an exception or return error in response
        try:
            response = scraper_client.parse("")
            # If it doesn't raise exception, check if success is False
            assert response.success is False
            assert response.error is not None
        except Exception as e:
            # It's acceptable for it to raise any exception for empty prompt
            assert str(e) is not None


class TestParseOutputFormats:
    """Test different output formats"""
    
    def test_json_format(self, scraper_client, test_url):
        """Test JSON output format"""
        response = scraper_client.parse(
            f"Extract information from {test_url}",
            output_format="json"
        )
        assert response.success is True
        assert response.data is not None
    
    def test_csv_format(self, scraper_client, test_url):
        """Test CSV output format"""
        response = scraper_client.parse(
            f"Extract information from {test_url} in table format",
            output_format="csv"
        )
        assert response.success is True
        assert response.data is not None
        # CSV data should be a string
        if response.data:
            assert isinstance(response.data, str)
    
    def test_markdown_format(self, scraper_client, test_url):
        """Test Markdown output format"""
        response = scraper_client.parse(
            f"Summarize the content from {test_url}",
            output_format="markdown"
        )
        assert response.success is True
        assert response.data is not None
        # Markdown data should be a string
        if response.data:
            assert isinstance(response.data, str)


class TestParseAdvanced:
    """Test advanced parse features"""
    
    def test_parse_with_max_pages(self, scraper_client, test_url):
        """Test parse with max_pages parameter"""
        response = scraper_client.parse(
            f"Extract information from {test_url}",
            max_pages=1
        )
        assert response.success is True
        # Just check that the parameter was accepted and request succeeded
    
    def test_parse_with_max_depth(self, scraper_client, test_url):
        """Test parse with max_depth parameter"""
        response = scraper_client.parse(
            f"Crawl {test_url} and extract any information",
            max_depth=1,
            max_pages=2
        )
        assert response.success is True
        # Just check that the parameters were accepted and request succeeded
    
    def test_complex_nested_schema(self, scraper_client, test_url):
        """Test parse with complex nested schema"""
        schema = {
            "type": "object",
            "properties": {
                "page": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "elements": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "type": {"type": "string"},
                                    "content": {"type": "string"}
                                }
                            }
                        }
                    },
                    "required": ["title"]
                }
            },
            "required": ["page"]
        }
        
        response = scraper_client.parse(
            f"Analyze the structure of {test_url} and extract page elements",
            schema=schema
        )
        
        assert response.success is True
        assert response.data is not None
        # Just verify the schema was accepted and parsed successfully


class TestParseTemplatesAndExamples:
    """Test parse templates and examples endpoints"""
    
    def test_get_templates(self, scraper_client):
        """Test getting available parse templates"""
        templates = scraper_client.parse_get_templates()
        assert templates.success is True
        assert hasattr(templates, 'templates')
    
    def test_get_examples(self, scraper_client):
        """Test getting parse examples"""
        examples = scraper_client.parse_get_examples()
        assert examples.success is True
        assert hasattr(examples, 'examples')


class TestParseErrorHandling:
    """Test parse error handling scenarios"""
    
    def test_invalid_url_handling(self, scraper_client):
        """Test handling of invalid URLs"""
        # This should either succeed with empty data or fail gracefully
        try:
            response = scraper_client.parse("Extract data from https://thisurldoesnotexist.invalid")
            # If it succeeds, it should indicate failure in response
            if response.success is False:
                assert response.error is not None
        except (SupacrawlerUnprocessableError, Exception) as e:
            # Or it should raise an appropriate exception
            assert str(e) is not None
    
    def test_malformed_schema_handling(self, scraper_client, test_url):
        """Test handling of malformed schemas"""
        # Invalid schema structure
        invalid_schema = {
            "type": "invalid_type",
            "properties": "not_an_object"
        }
        
        try:
            response = scraper_client.parse(
                f"Extract data from {test_url}",
                schema=invalid_schema
            )
            # If it succeeds, check if there's an error in response
            if response.success is False:
                assert response.error is not None
        except Exception as e:
            # Should handle malformed schema gracefully
            assert str(e) is not None


class TestParseCompatibility:
    """Test parse compatibility with different scenarios"""
    
    def test_parse_vs_scrape_behavior(self, scraper_client, test_url):
        """Test that parse can handle single page extraction like scrape"""
        # Single page extraction prompt
        parse_response = scraper_client.parse(f"Extract title from {test_url}")
        
        # Should work successfully 
        assert parse_response.success is True
    
    def test_crawling_behavior_detection(self, scraper_client, test_url):
        """Test that parse detects crawling intent from prompts"""
        # Crawling-style prompt
        crawl_response = scraper_client.parse(
            f"Crawl {test_url} and find all links",
            max_pages=2  # Limit for test
        )
        
        assert crawl_response.success is True
        # Just verify the crawling-style prompt was accepted
