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
    js_script = """window.scrollTo(0, document.body.scrollHeight);""".strip()
    
    def start_requests(self):
        url = "https://www.printables.com/model"

        yield SeleniumRequest(url=url, 
                            callback=self.parse, 
                            wait_until=EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")),
                            wait_time=10,
                            )

    def parse(self, response):
        base_url = "https://www.printables.com"

        self.driver = response.request.meta['driver']
        self.click_homePage_button()
        
        for _ in range(10):
            ActionChains(self.driver).scroll_by_amount(0, 10000).perform()
            sleep(1)

        # for product in response.css('print-card'):
        #     name = product.css('a.link.clamp-two-lines::text').get()
        #     likes = product.css('span.count.cursor-pointer::text').get()
        #     downloads = product.css('span.ml-1::text').getall()[1]
        #     link = product.css('a.link.clamp-two-lines::attr(href)').get()
        #     link = base_url + link
        
        for product in self.driver.find_elements(By.CSS_SELECTOR, "print-card"):
            name = product.find_element(By.CSS_SELECTOR, "a.link.clamp-two-lines").text
            likes = product.find_element(By.CSS_SELECTOR, "span.count.cursor-pointer").text
            downloads = product.find_elements(By.CSS_SELECTOR, "span.ml-1")[1].text
            link = product.find_element(By.CSS_SELECTOR, "a.link.clamp-two-lines").get_attribute('href')
            
            yield {
                "Name": name,
                "Likes Cound": likes,
                "Downloads": downloads,
                "Link": link
            }
    
    def click_homePage_button(self):
        
        wait = WebDriverWait(self.driver, 15)
        button = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
        try:
            button.click()
        except:
            pass
