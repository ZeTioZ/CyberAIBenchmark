import requests
from bs4 import BeautifulSoup


class PortSwiggerScrapper:
	def __init__(self, url: str):
		self.url = url
		self.title = ""
		self.extracted_data = []
		self.solution = ""
		
	def scrape(self):
		response = requests.get(self.url)
		if response.status_code != 200:
			print("Error while geting the response from the URL: " + self.url)
			return None, None, None
		soup = BeautifulSoup(response.text, features="html.parser")
		sections = soup.find_all('div', class_='section theme-white')
		
		for section in sections:
			self.title = section.find('h1', class_='heading-2').get_text(strip=True)
			label_level_div = section.find('div', class_='container-columns')
			buttons_left_div = section.find('div', class_='container-buttons-left')
			solution_div = section.find('div', class_='component-solution expandable-container')
			
			if label_level_div and buttons_left_div:
				extracted_content = []
				current_element = label_level_div.find_next_sibling()
				
				while current_element and current_element != buttons_left_div:
					extracted_content.append(current_element.get_text(strip=True))
					current_element = current_element.find_next_sibling()
					
				self.extracted_data.append('\n'.join(extracted_content))

			if solution_div:
				self.solution = solution_div.find('div', class_='content').get_text(strip=True)
		return self.title, self.extracted_data, self.solution
		
