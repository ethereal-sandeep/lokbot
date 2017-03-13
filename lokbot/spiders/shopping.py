# -*- coding: utf-8 -*-

# author: zero

import scrapy

from lokbot.items import LokbotItem, Status, LokbotTotalItem


class ShoppingSpider(scrapy.Spider):
    name = "shopping"
    allowed_domains = ["shopping.com"]
    keyword = None
    page = None

    def __init__(self, keyword=None, page=None, *args, **kwargs):
        super(ShoppingSpider, self).__init__(*args, **kwargs)

        if keyword is None and page is None:
            # print usage message
            print "\n---------------------------------------------------------------------------------\n" \
                  "|                Error: No arguments supplied !!                                   |\n" \
                  "|                                                                                  |\n" \
                  "| usage: $ scrapy crawl shopping -a keyword=\"iphone\" -a page=2 -o output.json    |\n" \
                  "| usage: $ scrapy crawl shopping -a keyword=\"iphone 7 plus\" -o total_result.json |\n" \
                  " ----------------------------------------------------------------------------------\n"
            self.start_urls = []
            return

        self.keyword = keyword
        self.start_urls = ['http://shopping.com/products?KW=%s' % keyword]

        if page is not None:
            self.page = page
            self.start_urls = ['http://shopping.com/products~PG-' + page + '?KW=%s' % keyword]

    def parse(self, response):
        msg = Status()
        if response.css('.nomatch::text').extract_first() is not None:
            msg["msg_text"] = "Sorry, There were no matches for your search " + self.keyword
            msg["msg_type"] = "FAILED"
        elif 'PG' in self.start_urls[0]:
            msg["msg_type"] = "SUCCESS"
            for item in response.css(".gridBox .gridItemBtm"):
                yield parse_node(item)
        else:
            msg["msg_type"] = "SUCCESS"
            value_list = response.css('#sortFiltersBox > span.numTotalResults::text').re(r'\w+')
            total_results = value_list[len(value_list) - 1]
            entity = LokbotTotalItem()
            entity['total_product_count'] = total_results
            entity['keyword'] = self.keyword
            yield entity

        yield msg
        pass


# methods
def parse_node(item):
    full_name = item.css('.quickLookGridItemFullName::text').extract_first()
    price = item.css('.productPrice a::text').extract_first()
    shipping_info = item.css('.taxShippingArea span::text').extract_first()
    company = item.css('.newMerchantName::text').extract_first()
    entity = LokbotItem()
    entity["product_title"] = full_name
    entity["product_price"] = price.strip() if price is not None else "NA"
    entity["product_shipping_info"] = shipping_info if shipping_info is not None else "No Shipping Info"
    entity["product_company"] = company
    return entity
