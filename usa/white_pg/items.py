# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnywhoItem(scrapy.Item):
    # define the fields for your item here like:
    #name = scrapy.Field()
    age=scrapy.Field()
    num=scrapy.Field()
    pass
