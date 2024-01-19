import scrapy
import pandas as pd


class BookSpider(scrapy.Spider):
    name = "bookcat"
    cats = []
    urls = []
    print("Scraping Started")

    def start_requests(self):
        url = "https://books.toscrape.com/index.html"
        yield scrapy.Request(url=url, callback=self.head)
    
    def head(self, response):
        
        for i, cat in enumerate(response.css('.side_categories ul li a::text').getall()):
            cat = cat.strip()
            cat += f"_{i+1}"
            self.cats.append(cat)

            temp = pd.DataFrame({'title': [], 'price': []})
            temp.to_csv(f"output/{cat[:-2]}_books.csv", index=False)
            
            url = f"https://books.toscrape.com/catalogue/category/books/{cat.lower()}/index.html"
            self.urls.append(url)

        # print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb:",self.cats)

        print(self.urls)

        for url in self.urls:
             yield scrapy.Request(url, callback=self.parse)
        


    def parse(self, response):        
        pass





        