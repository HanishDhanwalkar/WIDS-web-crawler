import scrapy
import pandas as pd


class BookSpider(scrapy.Spider):
    name = "bookcat"

    print("Scraping Started")

    def start_requests(self):

        urls = ["https://books.toscrape.com/index.html"]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            

    def parse(self, response):        
        cats  = []

        for cat in response.css('li a::text').getall():
            cats.append(cat.strip())

        print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb:",cats)

        for 


        