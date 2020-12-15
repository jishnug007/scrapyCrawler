import scrapy
from link_extractor import LinkExtractor


class BaseSpider(scrapy.Spider):
    name = "base"

    def start_requests(self):
        base_url = 'http://example.com/'
        yield scrapy.Request(url=base_url, callback=self.parse)

    def parse(self, response):
        links = LinkExtractor(response).get_links()
        for link in links:
            yield scrapy.Request(link.url, callback=self.parse)
