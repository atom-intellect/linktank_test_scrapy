from scrapy import Spider

class FailingSpider(Spider):
    name='another_2'
    start_urls = ['http://google.com']
    def parse(self, response):
        2/0
