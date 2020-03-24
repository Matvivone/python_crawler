# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class W4UItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    industry = scrapy.Field()
    region = scrapy.Field()
    country = scrapy.Field()
    size = scrapy.Field()
    last_publish_date = scrapy.Field()
    date_line = scrapy.Field()
    video = scrapy.Field()