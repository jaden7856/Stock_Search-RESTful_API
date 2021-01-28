# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YahooStockItem(scrapy.Item):
    symbol = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    open = scrapy.Field()
    day_min = scrapy.Field()
    day_max = scrapy.Field()
    volume = scrapy.Field()
    modify_date = scrapy.Field()
