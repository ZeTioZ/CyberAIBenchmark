class ScrappedData:
	def __init__(self, url, title, data, solution):
		self.url = url
		self.title = title
		self.data = data
		self.solution = solution

	def get_url(self):
		return self.url

	def get_title(self):
		return self.title

	def get_data(self):
		return self.data
	
	def get_solution(self):
		return self.solution

	def as_dict(self):
		return {
			"url": self.url,
			"title": self.title,
			"data": self.data,
			"solution": self.solution
		}
	
	def __str__(self):
		return f"{self.url}/n{self.title}: {self.data}/n/n{self.solution}"