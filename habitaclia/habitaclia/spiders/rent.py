import scrapy



class RentSpider(scrapy.Spider):
    name = "rent"
    allowed_domains = ["english.habitaclia.com"]
    start_urls = ["https://english.habitaclia.com/rent-flats-rubi.html"]

    def parse(self, response):
        links  = response.css('h3 a::text').getall()
        for link in links:
            yield scrapy.Request(link, callback=self.parse_item)
            
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_item(self, response):
        yield{
            'Title': response.css('h1').get(),
            'Area': response.css('li.feature:first-of-type strong::text').get()
        }