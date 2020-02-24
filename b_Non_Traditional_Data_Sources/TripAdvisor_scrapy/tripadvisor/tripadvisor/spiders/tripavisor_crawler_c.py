import scrapy


class QuotesSpider(scrapy.Spider):
    name = "tripadvisor_c"
    start_urls = [
        'https://www.tripadvisor.com/Restaurants-g294074-Bogota.html',
    ]

    def parse(self, response):
        for restaurant in response.css("a._15_ydu6b"):
            yield {
                'name': restaurant.css("a._15_ydu6b::text").get(),
                'name_array': restaurant.css("a._15_ydu6b::text").getall(),
                'url': restaurant.attrib['href']
            }