"""
Pytest configuration and shared fixtures for Supacrawler tests
"""

import os
import sys
from pathlib import Path

# Add src to Python path for imports
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

try:
    from dotenv import load_dotenv
    # Try to load .env file if it exists
    env_file = Path(__file__).parent.parent / ".env"
    if env_file.exists():
        load_dotenv(env_file)
    else:
        # Fall back to env.example for documentation
        load_dotenv(Path(__file__).parent.parent / "env.example")
except ImportError:
    pass  # dotenv not available, rely on system environment

import pytest
from supacrawler import SupacrawlerClient


@pytest.fixture
def scraper_client():
    """Client for scraper engine (localhost:8081) - no auth needed"""
    scraper_url = os.getenv('SCRAPER_URL', 'http://localhost:8081')
    return SupacrawlerClient(api_key="dummy-key", base_url=scraper_url)


@pytest.fixture
def backend_client():
    """Client for backend (localhost:8080) - needs API key AND scraper engine running"""
    backend_url = os.getenv('BACKEND_URL', 'http://localhost:8080/api')
    api_key = os.getenv('SUPACRAWLER_LOCAL_API_KEY')
    
    if not api_key:
        pytest.skip("SUPACRAWLER_LOCAL_API_KEY not set - skipping backend tests")
    
    if not api_key.startswith('sk_'):
        pytest.skip(f"Invalid API key format (should start with 'sk_'): {api_key[:10]}...")
    
    return SupacrawlerClient(api_key=api_key, base_url=backend_url)


@pytest.fixture
def test_url():
    """Standard test URL that works well for testing"""
    return "https://httpbin.org/html"
