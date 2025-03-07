class ScrappedData:
	def __init__(self, url, title, data):
		self.url = url
		self.title = title
		self.data = data

	def get_url(self):
		return self.url

	def get_title(self):
		return self.title

	def get_data(self):
		return self.data
	
	def as_dict(self):
		return {
			"title": self.title,
			"data": self.data
		}
	
	def __str__(self):
		return f"{self.title}: {self.data}"