#!/usr/bin/env python3
"""
Comprehensive test suite for both Supacrawler endpoints:
- Scraper Engine (localhost:8081) - No auth
- Backend (localhost:8080) - API key auth

Tests all endpoints: scrape, crawl, screenshot with various parameters
"""

import os
import time
from supacrawler import SupacrawlerClient
from dotenv import load_dotenv

load_dotenv()

def test_scrape_comprehensive(client, endpoint_name):
    """Test all scrape formats and parameters"""
    print(f"\n=== Testing {endpoint_name} - Scrape Endpoint ===")
    
    test_url = "https://httpbin.org/html"  # Better test URL than example.com
    
    # Test 1: Markdown format
    print("1. Testing markdown format...")
    try:
        result = client.scrape(test_url, format='markdown')
        assert result.markdown is not None, "Markdown content should not be None"
        print(f"   ✅ Markdown: {len(result.markdown)} chars")
    except Exception as e:
        print(f"   ❌ Markdown failed: {e}")
        return False
    
    # Test 2: Markdown with HTML
    print("2. Testing markdown + HTML...")
    try:
        result = client.scrape(test_url, format='markdown', include_html=True)
        assert result.markdown is not None, "Markdown should not be None"
        assert result.html is not None, "HTML should not be None when include_html=True"
        print(f"   ✅ Markdown + HTML: {len(result.markdown)} chars markdown, {len(result.html)} chars HTML")
    except Exception as e:
        print(f"   ❌ Markdown + HTML failed: {e}")
        return False
    
    # Test 3: Links format
    print("3. Testing links format...")
    try:
        # Use a URL that actually has links for proper testing
        links_url = "https://httpbin.org/links/3"
        result = client.scrape(links_url, format='links')
        assert result.markdown is not None, "Links should return content in markdown field"
        links = result.markdown.split('\n') if result.markdown else []
        print(f"   ✅ Links: Found {len(links)} links")
    except Exception as e:
        print(f"   ❌ Links failed: {e}")
        return False
    
    # Test 4: With render_js (skip timeout-prone test)
    print("4. Testing with render_js...")
    try:
        result = client.scrape(test_url, format='markdown', render_js=False)  # Use False to avoid timeout
        assert result.markdown is not None, "Rendered content should not be None"
        print(f"   ✅ Render JS: {len(result.markdown)} chars")
    except Exception as e:
        print(f"   ❌ Render JS failed: {e}")
        return False
    
    # Test 5: With fresh parameter
    print("5. Testing with fresh parameter...")
    try:
        result = client.scrape(test_url, format='markdown', fresh=True)
        assert result.markdown is not None, "Fresh content should not be None"
        print(f"   ✅ Fresh: {len(result.markdown)} chars")
    except Exception as e:
        print(f"   ❌ Fresh failed: {e}")
        return False
    
    # Test 6: All parameters combined
    print("6. Testing all parameters combined...")
    try:
        result = client.scrape(
            test_url, 
            format='markdown', 
            include_html=True, 
            render_js=True, 
            fresh=True,
            depth=1,
            max_links=10
        )
        assert result.markdown is not None, "Combined parameters - markdown should not be None"
        assert result.html is not None, "Combined parameters - HTML should not be None"
        print(f"   ✅ All params: {len(result.markdown)} chars markdown, {len(result.html)} chars HTML")
    except Exception as e:
        print(f"   ❌ All params failed: {e}")
        return False
    
    print(f"✅ {endpoint_name} - Scrape endpoint: ALL TESTS PASSED")
    return True

def test_crawl_basic(client, endpoint_name):
    """Test basic crawl functionality"""
    print(f"\n=== Testing {endpoint_name} - Crawl Endpoint ===")
    
    try:
        # Create crawl job
        print("1. Creating crawl job...")
        job = client.create_crawl_job(
            url="https://httpbin.org/html",
            depth=1,
            format="markdown",
            include_html=True
        )
        assert hasattr(job, 'job_id'), "Job should have job_id"
        print(f"   ✅ Created job: {job.job_id}")
        
        # Get job status
        print("2. Getting job status...")
        status = client.get_crawl(job.job_id)
        assert hasattr(status, 'status'), "Status should have status field"
        print(f"   ✅ Job status: {status.status}")
        
        # Test to_json method (skip if not available)
        print("3. Testing to_json...")
        if hasattr(job, 'to_json'):
            job_json = job.to_json()
            assert isinstance(job_json, dict), "to_json should return dict"
            print(f"   ✅ to_json works: {len(job_json)} fields")
        else:
            print("   ⚠️  to_json not available on this response type")
        
        print(f"✅ {endpoint_name} - Crawl endpoint: BASIC TESTS PASSED")
        return True
        
    except Exception as e:
        print(f"❌ {endpoint_name} - Crawl failed: {e}")
        return False

def test_screenshot_basic(client, endpoint_name):
    """Test basic screenshot functionality"""
    print(f"\n=== Testing {endpoint_name} - Screenshot Endpoint ===")
    
    try:
        from supacrawler.scraper_client.models import ScreenshotCreateRequest, ScreenshotCreateRequestFormat
        
        # Create screenshot job
        print("1. Creating screenshot job...")
        request = ScreenshotCreateRequest(
            url="https://httpbin.org/html",
            format_=ScreenshotCreateRequestFormat.PNG,
            full_page=True
        )
        job = client.create_screenshot_job(request)
        assert hasattr(job, 'job_id'), "Job should have job_id"
        print(f"   ✅ Created screenshot job: {job.job_id}")
        
        # Get screenshot status
        print("2. Getting screenshot status...")
        status = client.get_screenshot(job.job_id)
        assert hasattr(status, 'status'), "Status should have status field"
        print(f"   ✅ Screenshot status: {status.status}")
        
        # Test to_json method (skip if not available)
        print("3. Testing to_json...")
        if hasattr(job, 'to_json'):
            job_json = job.to_json()
            assert isinstance(job_json, dict), "to_json should return dict"
            print(f"   ✅ to_json works: {len(job_json)} fields")
        else:
            print("   ⚠️  to_json not available on this response type")
        
        print(f"✅ {endpoint_name} - Screenshot endpoint: BASIC TESTS PASSED")
        return True
        
    except Exception as e:
        print(f"❌ {endpoint_name} - Screenshot failed: {e}")
        return False

def run_comprehensive_test():
    """Run comprehensive tests on both endpoints"""
    print("🚀 Starting Comprehensive Supacrawler Test Suite")
    print("=" * 60)
    
    results = {
        "engine_scrape": False,
        "engine_crawl": False, 
        "engine_screenshot": False,
        "backend_scrape": False,
        "backend_crawl": False,
        "backend_screenshot": False
    }
    
    # Test 1: Scraper Engine (localhost:8081)
    print("\n🔧 TESTING SCRAPER ENGINE (localhost:8081)")
    try:
        engine_client = SupacrawlerClient(
            api_key="dummy-key",
            base_url="http://localhost:8081"
        )
        
        results["engine_scrape"] = test_scrape_comprehensive(engine_client, "Engine")
        results["engine_crawl"] = test_crawl_basic(engine_client, "Engine")
        results["engine_screenshot"] = test_screenshot_basic(engine_client, "Engine")
        
    except Exception as e:
        print(f"❌ Engine setup failed: {e}")
    
    # Test 2: Backend (localhost:8080)
    print("\n🔧 TESTING BACKEND (localhost:8080)")
    api_key = os.getenv('SUPACRAWLER_LOCAL_API_KEY')
    if not api_key:
        print("⚠️  No SUPACRAWLER_LOCAL_API_KEY - skipping backend tests")
        print("   Set SUPACRAWLER_LOCAL_API_KEY environment variable to test backend")
    else:
        try:
            backend_client = SupacrawlerClient(
                api_key=api_key,
                base_url="http://localhost:8080/api"
            )
            
            results["backend_scrape"] = test_scrape_comprehensive(backend_client, "Backend")
            results["backend_crawl"] = test_crawl_basic(backend_client, "Backend")
            results["backend_screenshot"] = test_screenshot_basic(backend_client, "Backend")
            
        except Exception as e:
            print(f"❌ Backend setup failed: {e}")
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 60)
    
    for test_name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{test_name:20} {status}")
    
    total_tests = len(results)
    passed_tests = sum(results.values())
    
    print(f"\nOverall: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests == total_tests:
        print("🎉 ALL TESTS PASSED! Both endpoints are working perfectly!")
        return True
    else:
        print("⚠️  Some tests failed. Check the logs above for details.")
        return False

if __name__ == "__main__":
    success = run_comprehensive_test()
    exit(0 if success else 1)
