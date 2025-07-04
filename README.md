"""
📚 Book Scraper from "Books to Scrape"

This Python script scrapes book information — including the title, price, and rating — 
from the website https://books.toscrape.com, which is designed for web scraping practice.

🔍 What It Does:
----------------
- Iterates through all pages on the site
- Extracts the book title, price, and star rating
- Converts star ratings from text ("One", "Two", etc.) to numeric values
- Saves the extracted data to a CSV file named 'products.csv'

🔧 Key Components:
------------------
- `get_star_rating`: Converts rating string to integer
- `extract_books_from_page(page_number)`: Scrapes one page of results
- `scrape_all_books()`: Loops through all available pages and aggregates results
- Output file: `products.csv` (with columns: Name, Price, Rating)

📦 Requirements:
----------------
- requests
- beautifulsoup4

Install with:
```bash
pip install requests beautifulsoup4
