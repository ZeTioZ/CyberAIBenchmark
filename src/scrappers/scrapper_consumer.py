from .portswigger_scrapper import PortSwiggerScrapper
from .pentesterlab_scrapper import PentesterLabScrapper

class ScrapperConsumer:
	def __init__(self):
		self.title = ""
		self.extracted_data = []
		self.solution = ""

	def scrape(self, url: str):
		domain = url.split("/")[2]
		match domain:
			case "portswigger.net":
				self.title, self.extracted_data, self.solution = PortSwiggerScrapper(url).scrape()
			case "pentesterlab.com":
				self.title, self.extracted_data, self.solution = PentesterLabScrapper(url).scrape()
			case _:
				raise ValueError(f"Unsupported URL: {url}")
		return self.title, self.extracted_data, self.solution

	def get_title(self):
		return self.title

	def get_extracted_data(self):
		return self.extracted_data

	def get_solution(self):
		return self.solution
