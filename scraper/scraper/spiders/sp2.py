from scrapy import Spider

class FailingSpider(Spider):
    name='sp2'
    start_urls = ['http://google.com']
    def parse(self, response):
        1/0
