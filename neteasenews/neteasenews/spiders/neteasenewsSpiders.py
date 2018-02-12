# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from neteasenews.items import NeteasenewsItem


class Neteasenews(CrawlSpider):
    name = 'neteasenews'
    start_urls = ['http://news.163.com/rank/']
    url = 'http://news.163.com/'

    def parse(self, response):
        item = NeteasenewsItem()
        selector = Selector(response)
        articles = selector.xpath('//tr')

        for lines in articles:
            try:
                ls = lines.xpath('td[@class="red"]')
                item['sort'] = ls.xpath('span/text()').extract()
                item['title'] = ls.xpath('a/text()').extract()
                item['herf'] = ls.xpath('a/@href').extract()
                if item['title'] == []:
                    ls = lines.xpath('td[@class="gray"]')
                    item['sort'] = ls.xpath('span/text()').extract()
                    item['title'] = ls.xpath('a/text()').extract()
                    item['herf'] = ls.xpath('a/@href').extract()
                item['dianji'] = lines.xpath('td[@class="cBlue"]/text()').extract()
                item['huifu'] = lines.xpath('td[@class="cBlue"]/text()').extract()
                yield item
            except:
                continue
