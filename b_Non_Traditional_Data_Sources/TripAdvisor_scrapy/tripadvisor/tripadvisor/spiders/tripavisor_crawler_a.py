# encoding: utf-8

##################################################
# This script corresponds to a "spider" component for the scrapy platform and
# allows to extract different components from the tripadvisor web platform
# a. The spider simply calls out elements (hyperlinks) corresponding to a class (_15_ydu6b)
# Documentation about scrapy and the tutorial used to develop this script
# visit: https://docs.scrapy.org/en/latest/intro/tutorial.html
##################################################
#
##################################################
# Author: Iacopo Testi and Diego Pajarito
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.3.0
# Maintainer: Diego Pajarito
# Email: diego.pajarito@iaac.net
# Status: development
##################################################

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "tripadvisor_a"
    # This variable stores the URLS to search in
    start_urls = [
        'https://www.tripadvisor.com/Restaurants-g294074-Bogota.html',
    ]

    def parse(self, response):
        # This loop goes through the list of restaurants labeled using classes
        for restaurant in response.css("a._15_ydu6b"):
            yield {
                'name': restaurant.get(),
                'url': restaurant.attrib['href']
            }
