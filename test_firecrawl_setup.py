#!/usr/bin/env python3
"""
Quick test to verify Firecrawl scraper setup
"""

import sys

def check_dependencies():
    """Check if required packages are installed"""
    print("Checking dependencies...")
    
    required = {
        'playwright': 'playwright',
        'asyncio': 'asyncio (built-in)',
    }
    
    missing = []
    
    for module, name in required.items():
        try:
            __import__(module)
            print(f"  ✅ {name}")
        except ImportError:
            print(f"  ❌ {name} - MISSING")
            missing.append(module)
    
    return missing

def test_basic_functionality():
    """Test basic scraper functionality without browser"""
    print("\nTesting scraper components...")
    
    try:
        from firecrawl_scraper import FirecrawlScraper, FirecrawlData, PricingTier, FeatureInfo
        
        # Test data classes
        data = FirecrawlData()
        assert data.company_name == "Firecrawl"
        print("  ✅ Data classes working")
        
        # Test to_dict
        data_dict = data.to_dict()
        assert 'company_name' in data_dict
        print("  ✅ Data serialization working")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False

def check_browser_installation():
    """Check if Playwright browsers are installed"""
    print("\nChecking browser installation...")
    
    try:
        from playwright.sync_api import sync_playwright
        
        with sync_playwright() as p:
            try:
                browser = p.chromium.launch()
                browser.close()
                print("  ✅ Chromium browser installed")
                return True
            except Exception as e:
                print(f"  ❌ Chromium not installed: {e}")
                print("\n  To install, run: playwright install chromium")
                return False
                
    except Exception as e:
        print(f"  ❌ Error checking browser: {e}")
        return False

def main():
    print("="*60)
    print("Firecrawl Scraper Setup Test")
    print("="*60)
    
    # Check dependencies
    missing = check_dependencies()
    
    if missing:
        print("\n❌ Missing dependencies. Install with:")
        print(f"   pip install {' '.join(missing)}")
        return 1
    
    # Test functionality
    if not test_basic_functionality():
        print("\n❌ Scraper component test failed")
        return 1
    
    # Check browser
    if not check_browser_installation():
        print("\n⚠️  Browser not installed. Run:")
        print("   playwright install chromium")
        print("\n   Or install all browsers:")
        print("   playwright install")
        return 1
    
    print("\n" + "="*60)
    print("✅ All tests passed! Ready to scrape Firecrawl.")
    print("="*60)
    print("\nNext steps:")
    print("  1. Run: python firecrawl_scraper.py")
    print("  2. Wait for scraping to complete")
    print("  3. Run: python firecrawl_analyzer.py")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
