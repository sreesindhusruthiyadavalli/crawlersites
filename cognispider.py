from scrapy.spiders import BaseSpider
from scrapy.selector import Selector
from scrapy.selector import HtmlXPathSelector
from crawlsite.items import CrawlsiteItem

class CogniSpider(BaseSpider):
	name = "cogni"
	allowed_domains = ["http://www.cognizant.com/careers"]
	start_urls = ["https://cognizant.taleo.net/careersection/indapac_itbpo_ext_career/\
						moresearch.ftl?lang=en#"]

	def parse(self, response):
		hs = Selector(response)
		#links = hs.xpath(".//*[@id='requisitionListInterface.listRequisition']")
		links = hs.xpath("//*[@class = 'titlelink']")
		#print links
		items = []
		for x in links:
			#print x
			item =  CrawlsiteItem()
			#item["title"] = x.xpath(".//span[@class = 'titlelink']/a//text()").extract()
			
			#item["location"] = hs.xpath('.//*[@class = "morelocation"]/span/text()').extract()
			#item["date"] = hs.xpath('.//*[contains(@id, "requisitionListInterface.reqPostingDate")]/text()').extract()
			#item["reqid"] = hs.xpath('.//*[contains(@id, "requisitionListInterface.reqContestNumberValue")]/text()').extract()
			items.append(item)
		return items	

		#https://cognizant.taleo.net/careersection/indapac_itbpo_ext_career/moresearch.ajax
		#https://cognizant.taleo.net/careersection/indapac_itbpo_ext_career/moresearch.ftl?lang=en#
		#.//*[@id='requisitionListInterface.reqTitleLinkAction.row25']

