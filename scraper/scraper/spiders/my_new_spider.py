from scrapy import Spider

class FailingSpider(Spider):
    name='my_new_spider'
    start_urls = ['http://google.com']
    def parse(self, response):
      1/0
