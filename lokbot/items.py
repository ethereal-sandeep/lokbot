# -*- coding: utf-8 -*-

# author: zero

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LokbotItem(scrapy.Item):
    # product model here
    product_title = scrapy.Field()
    product_price = scrapy.Field()  # price in dollar
    product_shipping_info = scrapy.Field()
    product_company = scrapy.Field()
    pass


class LokbotTotalItem(scrapy.Item):
    # total result count model here
    keyword = scrapy.Field()
    total_product_count = scrapy.Field()
    pass


class Status(scrapy.Item):
    # common status message here
    msg_text = scrapy.Field()
    msg_type = scrapy.Field()
    pass
