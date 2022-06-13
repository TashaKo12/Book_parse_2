import os

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlsplit, unquote


def parse_book_category(category_url):
    response = requests.get(category_url)
    response.raise_for_status()
    page_code = BeautifulSoup(response.text, "lxml")

    books_urls = []

    books = page_code.select("table.d_book")
    for book in books:
        book_id = book.find("a")["href"]
        books_urls.append(urljoin(category_url, book_id))

   

def main():
    category_url = "https://tululu.org/l55/"
    parse_book_category(category_url)


if __name__ == "__main__":
    main()
