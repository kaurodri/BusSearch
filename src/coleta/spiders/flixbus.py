import scrapy


class FlixbusSpider(scrapy.Spider):
    name = "flixbus"
    start_urls = ["https://www.flixbus.com.br"]

    def parse(self, response):

        placeholder="Brasília, DF"