from scrapy.item import Item, Field

class LocspiderItem(Item):
	continent = Field()
	state = Field()
	city = Field()
	domain = Field()
pass