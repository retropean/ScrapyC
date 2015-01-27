from scrapy.spider import Spider
from scrapy.selector import Selector

from items import LocspiderItem

import datetime
import time

class LocSpider(Spider):
	name = "locspider"
#	download_delay = 2
	allowed_domains = ["http://www.craigslist.org/about/sites"]
	start_urls = ["http://www.craigslist.org/about/sites"]

	def __init__(self):
		Spider.__init__(self)
		
	def __del__(self):
		Spider.__del__(self)

	def parse(self, response):
		sel = Selector(response)
		sites = sel.xpath('//div/ul/li')
#		sites = sel.xpath('//section[@class="body"]/h1')
#		sites = sel.xpath('//section[@class="body"]')
		items = []
		for site in sites:
			item = LocspiderItem()
			item['continent'] = map(unicode.strip, site.xpath('../../../../h1[last()]/text()').extract())
#			item['state'] = map(unicode.strip, site.xpath('../../h4[1]/text()').extract())
			item['state'] = map(unicode.strip, site.xpath('h4/text()[preceding-sibling::../../text()]').extract())
			item['city'] = map(unicode.strip, site.xpath('.//text()').extract())
			item['domain'] = map(unicode.strip, site.xpath('.//@href').extract())
			items.append(item)
		return items
'''			for con in sel.xpath('.//h1/h4/li'):
				item['continent'] = map(unicode.strip, site.xpath('.//h1/text()').extract())
				for s in sel.xpath('.//h4/text()'):
					item['state'] = map(unicode.strip, site.xpath('.//h4/text()').extract())
#					for cit in site.xpath('.//li/a/@href'):
#						item['city'] = map(unicode.strip, site.xpath('.//li/a/text()').extract())
#						item['domain'] = map(unicode.strip, site.xpath('.//li/a/@href').extract())'''