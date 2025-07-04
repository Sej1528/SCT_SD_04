import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = 'https://books.toscrape.com/catalogue/page-{}.html'
HEADERS = ['Name', 'Price', 'Rating']
OUTPUT_FILE = 'products.csv'

def get_star_rating(star_class):
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return rating_map.get(star_class, 0)

def extract_books_from_page(page_number):
    url = BASE_URL.format(page_number)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    books = soup.select('.product_pod')
    data = []

    for book in books:
        name = book.h3.a['title']
        price = book.select_one('.price_color').text.strip()
        rating_class = book.p['class'][1]
        rating = get_star_rating(rating_class)

        data.append([name, price, rating])
    
    return data

def scrape_all_books():
    all_books = []
    page = 1

    while True:
        print(f"Scraping page {page}...")
        books = extract_books_from_page(page)
        if not books:
            break
        all_books.extend(books)
        page += 1

    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(HEADERS)
        writer.writerows(all_books)

    print(f"Scraped {len(all_books)} products and saved to '{OUTPUT_FILE}'.")

if __name__ == "__main__":
    scrape_all_books()
