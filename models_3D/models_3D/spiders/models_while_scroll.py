import scrapy
from scrapy.http import HtmlResponse
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Models3dSpider(scrapy.Spider):
    name = "while_scroll"
    allowed_domains = ["www.printables.com"]
    seen_items = set()
    
    def start_requests(self):
        
        url = "https://www.printables.com/model"
        yield SeleniumRequest(url=url, 
                            callback=self.parse, 
                            wait_until=EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")),
                            wait_time=5,
                            )

    def parse(self, response):

        while True:
            items_number = len(self.seen_items)
            driver = response.meta['driver']
            yield from self.extract_items(driver)
            self.scroll_while_extracting(driver, 1500, 0.5)
            new_items_number = len(self.seen_items)
            if items_number == new_items_number:
                break
            if items_number > 500:
                break

    def scroll_while_extracting(self, driver, pixels_to_scroll: int, wait_time: int):
        for _ in range(3):
            driver.execute_script(f'''
                                window.scrollTo(window.scrollY, window.scrollY + {pixels_to_scroll});
                                ''')
            sleep(wait_time)

    def extract_items(self, driver):
        
        base_url = "https://www.printables.com"

        html = driver.page_source
        response = HtmlResponse(url=driver.current_url, body=html, encoding='utf-8')
        models = response.css('print-card[badgesize="md"]')
        for model in models:    # loads 36 items
            name = model.css('a.link.clamp-two-lines::text').get()
            likes = model.css('span.count.cursor-pointer::text').get()
            downloads = model.css('span.ml-1::text').getall()[1]
            link = model.css('a.link.clamp-two-lines::attr(href)').get()
            link = base_url + link
            
            if link not in self.seen_items:
                self.seen_items.add(link)
                yield {
                    'name':  name,
                    'likes': likes,
                    'downloads': downloads,
                    'link': link
                }
