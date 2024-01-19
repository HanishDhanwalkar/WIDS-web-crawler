# WIDS-web-crawler

A web scraper to get all the book from 'https://books.toscrape.com/'

There are 2 spiders implemented:
1. To scrape all books with their names and price
2. To scrape all books of particular categories in their own category list with prices.

Requirements:
1. Scrapy
    ```
    pip install scrapy
    ```

To run the crawler:
1. Clone this repo
    ```
    git clone https://github.com/HanishDhanwalkar/WIDS-web-crawler.git
    ```

2.
    To scrape all the books run (Start terminal):
    ```
    cd books
    ```
    ```
    scrapy crawl books
    ```
    

    --OR--

    To scrape books category-wise run (Start terminal):
    ```
    cd bookcatwise
    ```
    ```
    scrapy crawl bookcat
    ```
    
    

