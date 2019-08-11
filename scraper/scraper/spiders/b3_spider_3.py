from scrapy import Spider

class FailingSpider(Spider):
    name='b3s3'
    start_urls = ['http://google.com']
    def parse(self, response):
        1/0
