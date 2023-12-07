import scrapy


location = 'ca'   # Specify location Here
# https://www.zillow.com/ca/fsbo/

class ZillowHomes(scrapy.Spider):
    name = 'zillowhomes'    
    start_urls=[f'https://www.zillow.com/{location}/fsbo/']
    
    def parse(self, response):
        links = response.xpath('//a[@class="StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0 jnnxAW property-card-link"]/@href').getall()
        
        for link in links:
            print(link)
            yield {
                'link': link,
            }
            # yield scrapy.Request(link, callback=self.parse_item)
        
        next_link = response.xpath('//a[@class="StyledButton-c11n-8-84-3__sc-wpcbcc-0 dZFSon PaginationButton-c11n-8-84-3__sc-si2hz6-0 wfluH"]/@href').get()
        if next_link is not None:
            print(next_link)
            yield response.follow(next_link, callback=self.parse)
# /ca/fsbo/2_p/
    def parse_item(self, response):
        pass