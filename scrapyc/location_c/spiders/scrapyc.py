from scrapy.spider import Spider
from scrapy.selector import Selector

from items import CLItem

import datetime
import time

class CLSpider(Spider):
	name = "scrapyloc"
#	download_delay = 2
	allowed_domains = ["http://www.craigslist.org/about/sites"]
	start_urls = ["http://www.craigslist.org/about/sites"]

#	def __init__(self):
	def __init__(self):
		Spider.__init__(self)
		
	def __del__(self):
		Spider.__del__(self)

	def parse(self, response):
		sel = Selector(response)
		sites = sel.xpath('//section[@class="body"]')
		items = []
		for site in sites:
			item = CLItem()
			item['continent'] = map(unicode.strip, site.xpath('.//h1/text()').extract())
			item['state'] = map(unicode.strip, site.xpath('.//h4/text()').extract())
			item['city'] = map(unicode.strip, site.xpath('.//h4/li/text()').extract())
			item['domain'] = map(unicode.strip, site.xpath('.//h4/li/text()').extract())
			items.append(item)
		return items