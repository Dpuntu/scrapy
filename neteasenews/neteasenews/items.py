# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NeteasenewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    sort = scrapy.Field()
    title = scrapy.Field()
    herf = scrapy.Field()
    dianji = scrapy.Field()
    huifu = scrapy.Field()
    pass
