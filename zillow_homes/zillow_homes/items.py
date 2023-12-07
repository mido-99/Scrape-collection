# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZillowHomesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    address = scrapy.Field
    bds = scrapy.Field
    ba = scrapy.Field
    price = scrapy.Field
    sqft = scrapy.Field
    type = scrapy.Field
    lot = scrapy.Field
    yearbuilt = scrapy.Field
    days = scrapy.Field
    overview = scrapy.Field
    phone = scrapy.Field
    link = scrapy.Field
