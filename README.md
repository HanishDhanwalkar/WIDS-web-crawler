# WIDS-web-crawler

A web scraper to get all the book from 'https://books.toscrape.com/'

There are 2 spiders implemented:
1. To scrape all books with their names and price
2. To scrape all books of particular categories in their own category list with prices.

To run the crawler:
1. Clone this repo
2a. To scrape all the books run:
    cd books
    scrapy crawl books

2b. To scrape books category-wise run:
    cd bookcatwise
    scrapy crawl bookcat

