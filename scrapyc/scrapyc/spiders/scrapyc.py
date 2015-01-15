from scrapy.spider import Spider
from scrapy.selector import Selector

from scrapyc.items import CLItem

import datetime
import time

class CLSpider(Spider):
	name = "scrapyc"
	download_delay = 2
	allowed_domains = ["craigslist.org"]
	start_urls = []

	def __init__(self):
		for location in locations:
			# This will produce a list of [origin, dest], so grab those and use them
			# as falues for pluggin in to the url_pattern
			self.start_urls.append(url_pattern.format(origin=location[0],
					                             dest=location[1], day=readday,
					                             month=readmonth, year=readyear))
			# All done, start_urls now is what was before, but adding a new
			# dest/origin won't be tedious and changing global URL parameters is
			# done in the url_pattern

	def parse(self, response):
		sel = Selector(response)
		sites = sel.xpath('//ul[@class="journey standard none"]|//ul[@class="journey standard seat"]')
		items = []
		for site in sites:
			item = CLItem()
			item['title'] = map(unicode.strip, site.xpath('.//li[@class="two"]/p[1]/text()[3]').extract())
			item['price'] = map(unicode.strip, site.xpath('.//li[@class="two"]/p[1]/text()[5]').extract())
			item['location'] = map(unicode.strip, site.xpath('.//li[@class="two"]/p[1]/text()[2][normalize-space()]').extract())
			item['postdate'] = map(unicode.strip, site.xpath('.//p[@class="arrive"]/text()[3]').extract())
			item['odometer'] = map(unicode.strip, site.xpath('.//p[@class="arrive"]/text()[5]').extract())
			item['color'] = map(unicode.strip, site.xpath('.//p[@class="arrive"]/text()[2]').extract())
			item['transmission'] = map(unicode.strip, site.xpath('.//li[@class="three"]/p/text()').extract())
			item['title'] = map(unicode.strip, site.xpath('.//li[@class="five"]/p/text()[normalize-space()]').extract())
			item['cylinders'] = str(datetime.datetime.now().time())
			item['drive'] = map(unicode.strip, site.xpath('.//li[@class="three"]/p/text()').extract())
			item['fuel'] = map(unicode.strip, site.xpath('.//li[@class="five"]/p/text()[normalize-space()]').extract())
			item['type'] = str(datetime.datetime.now().time())
			item['datescraped'] = str(datetime.datetime.now().date())
			item['urlscraped'] = str(response.url)
			items.append(item)
		return items