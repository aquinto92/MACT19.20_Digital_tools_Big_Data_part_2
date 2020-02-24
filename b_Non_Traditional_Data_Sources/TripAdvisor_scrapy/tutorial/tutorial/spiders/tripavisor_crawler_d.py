import scrapy

class QuotesSpider(scrapy.Spider):
    name = "tripadvisor_d"
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

        next_page = response.xpath("//div[@class='unified pagination js_pageLinks']/a[@class='nav next rndBtn ui_button primary taLnk']").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
