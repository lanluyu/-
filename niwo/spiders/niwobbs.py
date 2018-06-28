# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from niwo.items import NiwoItem


class NiwobbsSpider(Spider):
    name = 'niwobbs'
    allowed_domains = ['http://bbs.niiwoo.com']

    def start_requests(self):
        for i in range(3,449):
            basic_url = 'http://bbs.niiwoo.com/forum.php?gid=1&page='
            start_url = basic_url+str(i)
            yield Request(url=start_url,callback=self.parse,dont_filter=True)

    def parse(self, response):
        a = response.xpath('.//div[@class="pg"]/strong/text()').extract_first()
        print('正在爬取第',a,'页')
        posts = response.xpath('.//table[@class="wtab"]/tbody')
        for post in posts:
            item = NiwoItem()
            item['title'] = ''.join(post.xpath('.//div[@class="thread-tit"]/a/text()').extract())
            item['author'] = ''.join(post.xpath('.//div[@class="thread-nums"]/a[1]/text()').extract())
            item['visitors'] = ''.join(post.xpath('.//div[@class="thread-nums"]/a[2]/@title').extract())
            # 第1，2页的时间提取规则
            #item['lasttime'] = '最后回复时间：'+''.join(post.xpath('.//a[@class="time"]/span/span/@title').extract())
            #第三页之后的时间提取规则
            item['lasttime'] = ''.join(post.xpath('.//a[@class="time"]/span/text()').extract())
            item['url'] = 'http://bbs.niiwoo.com/'+''.join(post.xpath('.//div[@class="thread-tit"]/a/@href').extract())

            print(item)
            yield item




