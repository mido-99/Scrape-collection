import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from time import sleep


class Models3dSpider(scrapy.Spider):
    name = "models_3d"
    allowed_domains = ["www.printables.com"]
    
    def start_requests(self):
        url = "https://www.printables.com/model"
        yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        base_url = "https://www.printables.com"
        driver, wait = self.setup_driver(response)
        self.click_homePage_button(driver, wait)
        for _ in range(10):
            ActionChains(driver).scroll_by_amount(0, 10000).perform()
            sleep(0.5)

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
    
    def setup_driver(self, response):
        
        driver = response.request.meta['driver']
        wait = WebDriverWait(driver, 15)
        return driver, wait
        
    def click_homePage_button(self, driver, wait):
        
        button = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
        button.click()

    