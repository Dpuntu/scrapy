# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from jianshu.items import JianshuItem

class Jianshu(CrawlSpider):
    name = 'jianshu'
    start_urls = ['http://www.jianshu.com/top/monthly']
    url = 'http://www.jianshu.com'

    def parse(self, response):
        item = JianshuItem()
        selector = Selector(response)
        articles = selector.xpath('//ul[@class="note-list"]/li')

        for article in articles:
            title = article.xpath('div/a/text()').extract()
            url = article.xpath('div/a/@href').extract()

            # 下载所有热门文章的缩略图, 注意有些文章没有图片
            # try:
            #     image = article.xpath("a/img/@src").extract()
            #     urllib.urlretrieve(image[0], '/Users/apple/Documents/images/%s-%s.jpg' % (author[0], title[0]))
            # except:
            #     print('--no---image--')
            item['ccommentLimt'] = article.xpath('div/p/text()').extract()
            listtop = article.xpath('div/div/a/text()').extract()
            likeNum = article.xpath('div/div/span/text()').extract()

            author = article.xpath('div/div/div/a[@class="nickname"]/text()').extract()
            # readAndComment = article.xpath('div/div[@class="list-footer"]')
            # data = readAndComment[0].xpath('string(.)').extract()[0]

            item['title'] = title
            item['url'] = 'http://www.jianshu.com/' + url[0]
            item['author'] = author

            item['readNum'] = listtop[3]
            # 有的文章是禁用了评论的
            try:
                item['commentNum'] = listtop[5]
            except:
                item['commentNum'] = ''
            item['likeNum'] = likeNum[0]
            try:
                item['moneyNum'] = likeNum[1]
            except:
                item['moneyNum'] = ''

            yield item

        next_link = selector.xpath('//*[@id="list-container"]/div/button/@data-url').extract()

        if len(next_link) == 1:
            next_link = self.url + str(next_link[0])
            yield Request(next_link, callback=self.parse)
