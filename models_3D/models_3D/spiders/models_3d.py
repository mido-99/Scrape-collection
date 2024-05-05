from typing import Iterable
import scrapy
from scrapy.http import Request
from scrapy_selenium import SeleniumRequest


class Models3dSpider(scrapy.Spider):
    name = "models_3d"
    allowed_domains = ["www.printables.com"]
    
    def start_requests(self):
        url = "https://www.printables.com/model"
        yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        base_url = "https://www.printables.com"
        
        for product in response.css('print-card'):
            name = product.css('a.link.clamp-two-lines::text').get()
            likes = product.css('span.count.cursor-pointer::text').get()
            downloads = product.css('span.ml-1::text').getall()[1]
            link = product.css('a.link.clamp-two-lines::attr(href)').get()
            link = base_url + link
            
            yield {
                "Name": name,
                "Likes Cound": likes,
                "Downloads": downloads,
                "Link": link
            }