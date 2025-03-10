import argparse

class ArgumentsParser:
	def __init__(self):
		self.parser = argparse.ArgumentParser(description="Benchmark AI models with scraped data.")
		self.parser.add_argument("-m", "--models", default="./models.txt", help="Path to the models ids (from Hugging Face) text file.")
		self.parser.add_argument("-l", "--links", default="./links.txt", help="Path to the links to scrap text file.")
		self.parser.add_argument("-llm_url", "--llm_url", default="http://127.0.0.1:1234/v1/chat/completions", help="URL of the LLM endpoint.")
		self.parser.add_argument("-o", "--output", default="output", help="Output file name.")

	def parse_args(self):
		return self.parser.parse_args()