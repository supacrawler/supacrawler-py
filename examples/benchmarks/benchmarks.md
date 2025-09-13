Selenium 

Single Page Scraping Comparison
===================================
Test URL: https://supabase.com

Selenium WebDriver:
Title: Supabase | The Postgres Development Platform.
Time: 4.08s

SupaCrawler:
Title: Supabase | The Postgres Development Platform.
Time: 1.37s

Performance: SupaCrawler is 3.0x faster

Multi-Page Crawling Comparison
===================================
Test URL: https://docs.python.org
Max pages: 10

Selenium manual crawling:
Pages crawled: 10
Total time: 42.11s
Average per page: 4.21s


First Selenium page result:
URL: N/A
Title: N/A
Text Preview: dev (3.15)
pre (3.14)
3.13.7
3 ...

Metadata: {'url': 'https://docs.python.org', 'title': '3.13.7 Documentation', 'description': 'The official Python documentation.', 'keywords': None, 'headers': [{'h1': 'Python 3.13.7 documentation'}], 'word_count': 244, 'links_found': 70}

SupaCrawler built-in crawling:
Pages crawled: 10
Total time: 2.05s
Average per page: 0.20s

First SupaCrawler page result:
Markdown Preview: # Python 3.13.7 documentation
Welcome! This is the official documentation for Python 3.13.7.
**Documentation sections:**
[What's new in Python 3.13?](whatsnew/3.13.html)
Or [all "What's new" documents ...

Metadata: {'title': '3.13.7 Documentation', 'status_code': 200, 'description': 'The official Python documentation.', 'canonical': 'https://docs.python.org/3/index.html', 'favicon': 'https://docs.python.org/_static/py.svg', 'og_title': 'Python 3.13 documentation', 'og_description': 'The official Python documentation.', 'og_image': 'https://docs.python.org/3/_static/og-image.png', 'source_url': 'https://docs.python.org'}

Performance: SupaCrawler is 20.6x faster per page

# Part 3: A more comprehensive test for crawling multiple pages!
Let's try running for 50 pages on 3 different websites this time:
-  supacrawler.com
-  supabase.com
-  ai.google.dev

Multi-Site Crawling Comparison


============================================================
Benchmarking: https://supabase.com
Max pages: 50
============================================================

[Selenium] Manual crawling:
  Pages crawled: 50
  Total time: 241.49s
  Avg per page: 4.83s
  First page title: Supabase | The Postgres Development Platform.

[SupaCrawler] Built-in crawling:
  Pages crawled: 50
  Total time: 36.26s
  Avg per page: 0.73s
  First page markdown preview: # Build in a weekendScale to millions
Supabase is the Postgres development platform.
Start your project with a Postgres  ...

⚡ Performance: SupaCrawler is 6.7x faster per page

============================================================
Benchmarking: https://docs.python.org
Max pages: 50
============================================================

[Selenium] Manual crawling:
  Pages crawled: 50
  Total time: 206.45s
  Avg per page: 4.13s
  First page title: 3.13.7 Documentation

[SupaCrawler] Built-in crawling:
  Pages crawled: 50
  Total time: 41.33s
  Avg per page: 0.83s
  First page markdown preview: # Python 3.13.7 documentation
Welcome! This is the official documentation for Python 3.13.7.
**Documentation sections:** ...

⚡ Performance: SupaCrawler is 5.0x faster per page

============================================================
Benchmarking: https://ai.google.dev
Max pages: 50
============================================================

[Selenium] Manual crawling:
  Pages crawled: 50
  Total time: 455.67s
  Avg per page: 9.11s
  First page title: Gemini Developer API | Gemma open models  |  Google AI for Developers

[SupaCrawler] Built-in crawling:
  Pages crawled: 50
  Total time: 37.25s
  Avg per page: 0.74s
  First page markdown preview: [NewGemini 2.5 Flash Image (aka Nano Banana) is now available in the Gemini API!](https://ai.google.dev/gemini-api/docs/ ...

⚡ Performance: SupaCrawler is 12.2x faster per page

# Playwright
Single Page Scraping Comparison
===================================
Test URL: https://example.com

Playwright:
Title: Example Domain
Time: 7.58s

SupaCrawler:
Title: Example Domain
Time: 1.21s

Performance: SupaCrawler is 6.3x faster
Setup complexity: Playwright (browser install + 1GB), SupaCrawler (API key only)

Multi-Page Crawling Comparison
===================================
Test URL: https://docs.python.org
Max pages: 5

Playwright manual crawling:
Pages crawled: 5
Total time: 164.39s
Average per page: 32.88s

SupaCrawler built-in crawling:
Pages crawled: 5
Total time: 5.08s
Average per page: 1.02s
Performance: SupaCrawler is 32.4x faster per page
Playwright success rate: 100.0%
SupaCrawler success rate: 100.0%

# Part 3: A more comprehensive test for crawling multiple pages!
Let's try running for 50 pages on 3 different websites this time:
-  supacrawler.com
-  supabase.com
-  ai.google.dev


============================================================
Benchmarking: https://supabase.com
Max pages: 50
============================================================

[Playwright] Manual crawling:
Retry 1 for https://supabase.com/dashboard after 1s due to Page.goto: Timeout 30000ms exceeded.
Call log:
  - navigating to "https://supabase.com/dashboard", waiting until "networkidle"

Retry 2 for https://supabase.com/dashboard after 2s due to Page.goto: Timeout 30000ms exceeded.
Call log:
  - navigating to "https://supabase.com/dashboard", waiting until "networkidle"

Failed to scrape https://supabase.com/dashboard after 3 attempts
Retry 1 for https://supabase.com/dashboard/support/new after 1s due to Page.goto: Timeout 30000ms exceeded.
Call log:
  - navigating to "https://supabase.com/dashboard/support/new", waiting until "networkidle"

Retry 2 for https://supabase.com/dashboard/support/new after 2s due to Page.goto: Timeout 30000ms exceeded.
Call log:
  - navigating to "https://supabase.com/dashboard/support/new", waiting until "networkidle"

Failed to scrape https://supabase.com/dashboard/support/new after 3 attempts
  Pages crawled: 50
  Total time: 1871.31s
  Avg per page: 37.43s
  First page title: Supabase | The Postgres Development Platform.

[SupaCrawler] Built-in crawling:
  Pages crawled: 50
  Total time: 32.34s
  Avg per page: 0.65s
  First page markdown preview: # Build in a weekendScale to millions
Supabase is the Postgres development platform.
Start your project with a Postgres  ...

⚡ Performance: SupaCrawler is 57.9x faster per page


============================================================
Benchmarking: https://docs.python.org
Max pages: 50
============================================================

[Playwright] Manual crawling:
  Pages crawled: 50
  Total time: 2775.49s
  Avg per page: 55.51s
  First page title: 3.13.7 Documentation

[SupaCrawler] Built-in crawling:
  Pages crawled: 50
  Total time: 35.32s
  Avg per page: 0.71s
  First page markdown preview: # Python 3.13.7 documentation
Welcome! This is the official documentation for Python 3.13.7.
**Documentation sections:** ...

⚡ Performance: SupaCrawler is 78.6x faster per page


============================================================
Benchmarking: https://ai.google.dev
Max pages: 50
============================================================

[Playwright] Manual crawling:
Retry 1 for https://ai.google.dev/gemini-api/docs/video after 1s due to Page.goto: Timeout 30000ms exceeded.
Call log:
  - navigating to "https://ai.google.dev/gemini-api/docs/video", waiting until "networkidle"

Retry 2 for https://ai.google.dev/gemini-api/docs/video after 2s due to Page.goto: Timeout 30000ms exceeded.
Call log:
  - navigating to "https://ai.google.dev/gemini-api/docs/video", waiting until "networkidle"

Failed to scrape https://ai.google.dev/gemini-api/docs/video after 3 attempts
  Pages crawled: 50
  Total time: 1433.59s
  Avg per page: 28.67s
  First page title: Gemini Developer API | Gemma open models  |  Google AI for Developers

[SupaCrawler] Built-in crawling:
  Pages crawled: 50
  Total time: 36.44s
  Avg per page: 0.73s
  First page markdown preview: [NewGemini 2.5 Flash Image (aka Nano Banana) is now available in the Gemini API!](https://ai.google.dev/gemini-api/docs/ ...

⚡ Performance: SupaCrawler is 39.3x faster per page

# BeuatifulSoup


# Fair BeautifulSoup vs Supacrawler: Complete Performance Comparison

This notebook compares BeautifulSoup (with requests) against Supacrawler with similar retry logic that matches Supacrawler's exact implementation.

1. **Identical Retry Logic**: Uses the same exponential backoff (1s, 2s, 4s) and retry conditions as Supacrawler
2. **Smart Error Classification**: Only retries on retryable errors (429, 503, timeouts) - not 403/404
3. **Same Max Retries**: 3 attempts total, matching Supacrawler service
4. **Timeout Consistency**: Uses similar timeout patterns to Supacrawler's HTTP implementation

Note: BeautifulSoup + requests is similar to Supacrawler's simple HTTP scraping (no JavaScript), so this is a fair comparison for non-JS content.

{'title': 'Supabase | The Postgres Development Platform.', 'content': 'Supabase | The Postgres Development Platform.Product Developers Solutions PricingDocsBlog88.3KSign inStart your projectOpen main menuBuild in a weekendScale to millionsSupabase is the Postgres develop...', 'time': 0.25898218154907227, 'javascript_support': False, 'resource_usage': 'Low (HTTP only)'}
{'title': 'Supabase | The Postgres Development Platform.', 'content': '# Build in a weekendScale to millions\nSupabase is the Postgres development platform.\nStart your project with a Postgres database, Authentication, instant APIs, Edge Functions, Realtime subscriptions, ...', 'metadata': <supacrawler.types.PageMetadata object at 0x1184d6c10>, 'time': 0.3802957534790039, 'javascript_support': False, 'resource_usage': 'Zero local resources'}

Time difference: -0.12131357192993164 seconds
Supacrawler is 1.4684243958573073 times faster than BeautifulSoup

Beautifulsoup Content: 
Supabase | The Postgres Development Platform.Product Developers Solutions PricingDocsBlog88.3KSign inStart your projectOpen main menuBuild in a weekendScale to millionsSupabase is the Postgres develop...

Supacrawler Content: 
# Build in a weekendScale to millions
Supabase is the Postgres development platform.
Start your project with a Postgres database, Authentication, instant APIs, Edge Functions, Realtime subscriptions, ...

Multi-Site Crawling Comparison


============================================================
Benchmarking: https://nodejs.org/docs
Max pages: 50
============================================================

[BeautifulSoup] Manual crawling:
Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
Some characters could not be decoded, and were replaced with REPLACEMENT CHARACTER.
  Pages crawled: 50
  Total time: 109.19s
  Avg per page: 2.18s
  First page title: Index of /docs/
  Metadata: {'status_code': 200, 'word_count': 3454, 'headers': ['Index of /docs/']}

[SupaCrawler] Built-in crawling:
  Pages crawled: 50
  Total time: 65.51s
  Avg per page: 1.31s
  First page markdown preview: # Run JavaScript Everywhere
Node.js® is a free, open-source, cross-platform JavaScript runtime environment
that lets dev ...
  Metadata: {'title': 'Node.js — Run JavaScript Everywhere', 'status_code': 200, 'description': 'Node.js® is a free, open-source, cross-platform JavaScript runtime environment that lets developers create servers, web apps, command line tools and scripts.', 'canonical': 'https://nodejs.org/en', 'favicon': 'https://nodejs.org/static/images/favicons/favicon.png', 'og_title': 'Node.js — Run JavaScript Everywhere', 'og_description': 'Node.js® is a free, open-source, cross-platform JavaScript runtime environment that lets developers create servers, web apps, command line tools and scripts.', 'og_image': 'https://nodejs.org/en/next-data/og/announcement/Node.js%20%E2%80%94%20Run%20JavaScript%20Everywhere', 'twitter_title': 'Node.js — Run JavaScript Everywhere', 'twitter_description': 'Node.js® is a free, open-source, cross-platform JavaScript runtime environment that lets developers create servers, web apps, command line tools and scripts.', 'twitter_image': 'https://nodejs.org/static/images/logo-hexagon-card.png', 'source_url': 'https://nodejs.org'}

⚡ Performance: SupaCrawler is 1.7x faster per page

============================================================
Benchmarking: https://docs.python.org
Max pages: 50
============================================================

[BeautifulSoup] Manual crawling:
  Pages crawled: 50
  Total time: 3.61s
  Avg per page: 0.07s
  First page title: 3.13.7 Documentation
  Metadata: {'status_code': 200, 'word_count': 415, 'headers': ['Download', 'Docs by version', 'Other resources', 'Navigation', 'Python 3.13.7 documentation', 'Download', 'Docs by version', 'Other resources', 'Navigation']}

[SupaCrawler] Built-in crawling:
  Pages crawled: 50
  Total time: 7.09s
  Avg per page: 0.14s
  First page markdown preview: # Python 3.13.7 documentation
Welcome! This is the official documentation for Python 3.13.7.
**Documentation sections:** ...
  Metadata: {'title': '3.13.7 Documentation', 'status_code': 200, 'description': 'The official Python documentation.', 'canonical': 'https://docs.python.org/3/index.html', 'favicon': 'https://docs.python.org/_static/py.svg', 'og_title': 'Python 3.13 documentation', 'og_description': 'The official Python documentation.', 'og_image': 'https://docs.python.org/3/_static/og-image.png', 'source_url': 'https://docs.python.org'}

⚡ Performance: SupaCrawler is 0.5x faster per page

============================================================
Benchmarking: https://go.dev/doc/
Max pages: 50
============================================================

[BeautifulSoup] Manual crawling:
  Pages crawled: 50
  Total time: 25.10s
  Avg per page: 0.50s
  First page title: Documentation - The Go Programming Language
  Metadata: {'status_code': 200, 'word_count': 1929, 'headers': ['Documentation', 'Getting Started', 'Installing Go', 'Tutorial: Getting started', 'Tutorial: Create a module', 'Tutorial: Getting started with multi-module workspaces', 'Tutorial: Developing a RESTful API with Go and Gin', 'Tutorial: Getting started with generics', 'Tutorial: Getting started with fuzzing', 'Writing Web Applications', 'How to write Go code', 'A Tour of Go', 'Using and understanding Go', 'Effective Go', 'Frequently Asked Questions (FAQ)', 'Editor plugins and IDEs', 'Diagnostics', 'A Guide to the Go Garbage Collector', 'Managing dependencies', 'Fuzzing', 'Coverage for Go applications', 'Profile-guided optimization', 'References', 'Package Documentation', 'Command Documentation', 'Language Specification', 'Go Modules Reference', 'go.mod file reference', 'The Go Memory Model', 'Contribution Guide', 'Release History', 'Accessing databases', 'Tutorial: Accessing a relational database', 'Accessing relational databases', 'Opening a database handle', "Executing SQL statements that don't return data", 'Querying for data', 'Using prepared statements', 'Executing transactions', 'Canceling in-progress database operations', 'Managing connections', 'Avoiding SQL injection risk', 'Developing modules', 'Developing and publishing modules', 'Module release and versioning workflow', 'Managing module source', 'Organizing a Go module', 'Developing a major version update', 'Publishing a module', 'Module version numbering', 'Talks', 'A Video Tour of Go', 'Code that grows with grace', 'Go Concurrency Patterns', 'Advanced Go Concurrency Patterns', 'Codewalks', 'Language', 'Packages', 'Modules', 'Tools', 'Wiki', 'Non-English Documentation']}

[SupaCrawler] Built-in crawling:
  Pages crawled: 50
  Total time: 17.16s
  Avg per page: 0.34s
  First page markdown preview: # Build simple, secure, scalable systems with Go
-
An open-source programming language supported by Google
-
Easy to lea ...
  Metadata: {'title': 'The Go Programming Language', 'status_code': 200, 'description': 'Go is an open source programming language that makes it simple to build secure, scalable systems.', 'favicon': 'https://go.dev/images/favicon-gopher.png', 'og_title': 'The Go Programming Language', 'og_description': 'Go is an open source programming language that makes it simple to build secure, scalable systems.', 'og_image': 'https://go.dev/doc/gopher/gopher5logo.jpg', 'twitter_image': 'https://go.dev/doc/gopher/gopherbelly300.jpg', 'source_url': 'https://go.dev'}

⚡ Performance: SupaCrawler is 1.5x faster per page