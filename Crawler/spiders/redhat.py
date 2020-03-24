# -*- coding: utf-8 -*-
import scrapy
import urllib
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from w4u.items import W4UItem
from urllib.parse import urljoin

class RedhatSpider(CrawlSpider):
    name = 'redhat'
    allowed_domains = ['www.redhat.com']
    start_urls = ['https://www.redhat.com/en/success-stories',]
    
    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pager-next',)),
             callback="parse_start_url",
             follow=True),)
    
    def parse_start_url(self, response):
        arrayOfStories = response.css('a.rh-customer-success--component::attr(href)').getall()
        for url in arrayOfStories:
            # We make a request to each url and call the parse function on the http response.
            nuevaurl = urljoin('https://www.redhat.com/en/success-stories', url)
            yield Request(nuevaurl, callback=self.parsestoryindustry, meta={'urlpar': url})
            
                
    def parsestoryindustry(self,response):        

        item = W4UItem()
        url = response.meta.get('urlpar')
        item['url'] = url
        
        try:
             item['industry'] = response.css('dd::text')[0].extract()
        except Exception:
            pass  # or you could use 'continue'

        try:
            item['region'] = response.css('dd::text')[1].extract()
        except Exception:
            pass  # or you could use 'continue'        

        try:
            item['country'] = response.css('dd::text')[2].extract()
        except Exception:
            pass  # or you could use 'continue'        


        try:
            item['size'] = response.css('dd::text')[3].extract()
        except Exception:
            pass  # or you could use 'continue'        


        try:
            item['video'] = response.xpath('//iframe/@src').extract_first()
        except Exception:
            pass  # or you could use 'continue'        

        try:
            item['last_publish_date'] =  response.xpath("//meta[@name='last-publish-date']/@content")[0].extract()
        except Exception:
            pass  # or you could use 'continue'        
            
        try:
            item['date_line'] =  response.xpath("//meta[@name='dateline']/@content")[0].extract()
        except Exception:
            pass  # or you could use 'continue'        
        
        yield item