from scrapy.spider import Spider
from scrapy.selector import Selector

from items import CLItem

import datetime
import time

class CLSpider(Spider):
	name = "scrapyc"
	download_delay = 2
	allowed_domains = ["http://washingtondc.craigslist.org"]
	start_urls = ["http://washingtondc.craigslist.org/nva/cto/4844190688.html"]

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
			item['title'] = map(unicode.strip, site.xpath('.//h2[@class="postingtitle"]/text()').extract())
			item['price'] = map(unicode.strip, site.xpath('.//h2[@class="postingtitle"]/text()').extract())
			item['location'] = map(unicode.strip, site.xpath('.//h2[@class="postingtitle"]/text()').extract())
			item['postdate'] = map(unicode.strip, site.xpath('.//p[@class="postinginfo"]/text()').extract())
			item['odometer'] = map(unicode.strip, site.xpath('.//p[@class="attrgtoup"]/span/text()[1]').extract())
			item['color'] = map(unicode.strip, site.xpath('.//p[@class="attrgtoup"]/text()[2]').extract())
			item['transmission'] = map(unicode.strip, site.xpath('.//p[@class="attrgtoup"]/text()[3]').extract())
			item['title'] = map(unicode.strip, site.xpath('.//p[@class="attrgtoup"]/text()[4]').extract())
			item['cylinders'] = map(unicode.strip, site.xpath('.//p[@class="attrgtoup"]/text()[5]').extract())
			item['drive'] = map(unicode.strip, site.xpath('.//p[@class="attrgtoup"]/text()[6]').extract())
			item['fuel'] = map(unicode.strip, site.xpath('.//p[@class="attrgtoup"]/text()[7]').extract())
			item['type'] = map(unicode.strip, site.xpath('.//p[@class="attrgtoup"]/text()[8]').extract())
#			item['postid'] = 
#			item['updatedate'] = 
			item['datescraped'] = str(datetime.datetime.now().date())
			item['urlscraped'] = str(response.url)
			items.append(item)
		return items