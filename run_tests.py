#!/usr/bin/env python3
"""
Test runner for Supacrawler Python SDK
Can be used manually or by pre-commit hooks
"""

import os
import sys
import subprocess
from pathlib import Path

# Add src to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

try:
    from dotenv import load_dotenv
    env_file = Path(__file__).parent / ".env"
    if env_file.exists():
        load_dotenv(env_file)
        print("✅ Loaded .env file")
    else:
        load_dotenv(Path(__file__).parent / "env.example")
        print("⚠️  Using env.example (create .env for actual config)")
except ImportError:
    print("⚠️  python-dotenv not available, using system environment")


def check_environment():
    """Check if required environment variables are set"""
    print("\n🔧 Environment Check:")
    
    scraper_url = os.getenv('SCRAPER_URL', 'http://localhost:8081')
    backend_url = os.getenv('BACKEND_URL', 'http://localhost:8080/api')
    api_key = os.getenv('SUPACRAWLER_LOCAL_API_KEY')
    
    print(f"   Scraper URL: {scraper_url}")
    print(f"   Backend URL: {backend_url}")
    print(f"   API Key: {'✅ Set' if api_key else '❌ Missing (backend tests will skip)'}")
    
    return api_key is not None


def run_comprehensive_test():
    """Run the comprehensive test suite"""
    print("\n🧪 Running Comprehensive Test Suite...")
    print("=" * 60)
    
    test_file = Path(__file__).parent / "test" / "test_comprehensive.py"
    cmd = [sys.executable, str(test_file)]
    
    result = subprocess.run(cmd)
    return result.returncode == 0


def run_pytest_tests():
    """Run all pytest tests"""
    print("\n🧪 Running Pytest Test Suite...")
    print("=" * 60)
    
    test_dir = Path(__file__).parent / "test"
    cmd = [sys.executable, "-m", "pytest", str(test_dir), "-v", "--tb=short"]
    
    result = subprocess.run(cmd)
    return result.returncode == 0


def main():
    """Main test runner"""
    print("🚀 Supacrawler Python SDK Test Runner")
    print("=" * 60)
    
    # Check environment
    has_api_key = check_environment()
    
    # Run comprehensive test (our custom runner)
    print("\n" + "=" * 60)
    print("Running Comprehensive Tests (Custom Runner)")
    print("=" * 60)
    comprehensive_success = run_comprehensive_test()
    
    # Run pytest tests
    print("\n" + "=" * 60)
    print("Running Pytest Tests (All Test Files)")
    print("=" * 60)
    pytest_success = run_pytest_tests()
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    print(f"Comprehensive Tests: {'✅ PASS' if comprehensive_success else '❌ FAIL'}")
    print(f"Pytest Tests: {'✅ PASS' if pytest_success else '❌ FAIL'}")
    
    if not has_api_key:
        print("\n⚠️  Note: Backend tests were skipped due to missing SUPACRAWLER_LOCAL_API_KEY")
        print("   Set this environment variable to test backend functionality")
    
    overall_success = comprehensive_success and pytest_success
    
    if overall_success:
        print("\n🎉 ALL TESTS PASSED!")
        return 0
    else:
        print("\n❌ SOME TESTS FAILED!")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
