import argparse

class ArgumentsParser:
	def __init__(self):
		self.parser = argparse.ArgumentParser(description="Benchmark AI models with scraped data.")
		self.parser.add_argument("-m", "--models", default="./models.txt", help="Path to the models ids (from Hugging Face) text file.")
		self.parser.add_argument("-l", "--links", default="./links.txt", help="Path to the links to scrap text file.")
		self.parser.add_argument("-llm_prompt_url", "--llm_prompt_url", default="http://127.0.0.1:1234/v1/chat/completions", help="URL of the LLM endpoint.")
		self.parser.add_argument("-llm_get_models_url", "--llm_get_models_url", default="http://localhost:1234/api/v0/models/", help="URL of the LLM endpoint.")
		self.parser.add_argument("-o", "--output", default="output", help="Output file name.")
		self.parser.add_argument("-preload", "--preload", action="store_true", help="Preload the model before sending the prompt request.")
		self.parser.add_argument("-evaluate", "--evaluate", action="store_true", help="Evaluate the model after sending the prompt request.")
		self.parser.add_argument("-evaluation_input", "--evaluation_input", default="./output/benchmarking_output.xlsx", help="Input for the evaluation process.")
		self.parser.add_argument("-no_benchmark", "--no_benchmark", default=False, action="store_true", help="Do not run the benchmark.")
		self.parser.add_argument("-custom_challenges", "--custom_challenges", help="Use json formatted custom challenges.")

	def parse_args(self):
		return self.parser.parse_args()