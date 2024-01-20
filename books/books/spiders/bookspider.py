import scrapy
import pandas as pd


class BookSpider(scrapy.Spider):
    name = "books"

    print("Scraping Started")

    books = pd.DataFrame({'title': [], 'price': []})
    books.to_csv('books.csv', index=False)

    def start_requests(self):

        urls = ["https://books.toscrape.com/catalogue/page-1.html"]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            

    def parse(self, response):        

        books = pd.read_csv("books.csv")
        
        for book in response.css('article.product_pod'):
            title = book.css('h3 a::attr(title)').get()
            price = book.css('.price_color::text').get()

            books = books._append({'title': title, 'price': price}, ignore_index=True)
            books.to_csv('books.csv', index=False)

        next_page = response.css('li.next a::attr(href)').get()

        if next_page:
            # print("Searching " + next_page)
            yield scrapy.Request(url="https://books.toscrape.com/catalogue/" + next_page, callback=self.parse)

        else:
            books.to_csv('books.csv', index=False)


        