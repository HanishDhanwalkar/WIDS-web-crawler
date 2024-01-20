# WIDS-web-crawler

A web scraper to get all the book from 'https://books.toscrape.com/'

There are 2 spiders implemented to scrape in 2 differnet format:
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

2.  Start terminal 
    
    ```
    cd books
    ```
    To scrape all the books run:
    
    ```
    scrapy crawl books
    ```
    

    --OR--

    To scrape books category-wise run:
    ```
    scrapy crawl bookcat
    ```

All the books scraped are in books.csv (or bookscatwise.csv for category-wise)
    
    

