from typing import Any, Optional
import scrapy
import pandas as pd


class BookSpider(scrapy.Spider):
    name = "bookcat"

    def __init__(self):
        print("Scraping Started........................")

        books = pd.DataFrame({'title': [], 'category':[], 'price': []})
        books.to_csv('bookscatwise.csv', index=False)

    def start_requests(self):
        url = "https://books.toscrape.com/index.html"

        yield scrapy.Request(url=url, callback=self.head)
    
    def head(self, response):
        urls = response.css('ul.nav-list > li > ul > li > a::attr(href)').extract()
        # print(urls)

        for url in urls:
            yield scrapy.Request(f"https://books.toscrape.com/{url}", callback=self.parse) 

    def parse(self, response): 
        books = pd.read_csv("bookscatwise.csv")       
        for book in response.css('article.product_pod'):
            title = book.css('h3 a::attr(title)').get()
            price = book.css('.price_color::text').get()
            cat = response.css("h1::text").get()

            books = books._append({'title': title,'category':cat, 'price': price}, ignore_index=True)

            books.to_csv("bookscatwise.csv", index=False)
        next_page = response.css('li.next a::attr(href)').get()

        if next_page:
            # print("Searching\n " + next_page)
            url_ = response.url
            url_ = url_.split("/")
            url_ = "/".join(url_[:-1])
            url_ = url_ + "/"
            yield scrapy.Request(url=url_ + next_page, callback=self.parse)






        