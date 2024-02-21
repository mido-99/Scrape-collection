import scrapy



class RentSpider(scrapy.Spider):
    name = "rent"
    allowed_domains = ["english.habitaclia.com"]
    start_urls = ["https://english.habitaclia.com/rent-flats-rubi.html"]

    def parse(self, response):
        links  = response.css('section.list-items:first-of-type h3 a::attr(href)').getall()
        yield from response.follow_all(links, callback=self.parse_item)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_item(self, response):
        yield{
            'Title': response.css('h1::text').get(),
            'Area': response.css('li.feature:first-of-type strong::text').get()
        }