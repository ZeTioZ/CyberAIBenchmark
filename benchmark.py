import json
import pandas as pd
import requests
from bs4 import BeautifulSoup

from scrapped_data import ScrappedData


def scrape_info(url: str) -> tuple:
	response = requests.get(url)
	if response.status_code != 200:
		print("Error while getting the response from the URL: " + url)
		return None
	soup = BeautifulSoup(response.text, features="html.parser")
	
	sections = soup.find_all('div', class_='section theme-white')
	title = ""
	extracted_data = []
	
	for section in sections:
		title = section.find('h1', class_='heading-2').get_text(strip=True)
		label_level_div = section.find('div', class_='container-columns')
		buttons_left_div = section.find('div', class_='container-buttons-left')
		
		if label_level_div and buttons_left_div:
			extracted_content = []
			current_element = label_level_div.find_next_sibling()
			
			while current_element and current_element != buttons_left_div:
				extracted_content.append(current_element.get_text(strip=True))
				current_element = current_element.find_next_sibling()
				
			extracted_data.append('\n'.join(extracted_content))
	return title, extracted_data


def send_request(message: str, model: str="hermes-3-llama-3.2-3b", llm_url: str="http://127.0.0.1:1234/v1/chat/completions") -> dict:
	if not message:
		return {"error": "Message is empty"}
	if not model:
		return {"error": "Model is empty"}
	if not llm_url:
		return {"error": "LLM URL is empty"}
	
	payload = {
		"model": model,
		"messages": [
			{ "role": "system", "content": "" },
			{ "role": "user", "content": message }
		],
		"temperature": 0.7,
		"max_tokens": -1,
		"stream": False
	}

	headers = {
		"Content-Type": "application/json"
	}
	try:
		response = requests.post(llm_url, headers=headers, data=json.dumps(payload))
		if response.status_code == 200:
			return response.json()
		else:
			return {"error": "Request failed with status code " + str(response.status_code)}
	except Exception as e:
		return {"Error while sending request to the LLM model": str(e)}


def benchmark(models: list=[], urls: list=[]) -> None:
	scrapped_datas = []
	for url in urls:
		title, data = scrape_info(url)
		scrapped_datas.append(ScrappedData(url, title, ''.join(data)))

	data = []
	for model in models:
		for scrapped_data in scrapped_datas:
			response = send_request(scrapped_data.get_data(), model)
			bot_response = response.get("choices")[0].get("message").get("content") if response.get("choices") else "No response from the model"
			data.append({
				"Model": model,
				"URL": scrapped_data.get_url(),
				"Title": scrapped_data.get_title(),
				"Data": scrapped_data.get_data(),
				"AI Response": bot_response
			})
	df = pd.DataFrame(data)
	df.to_excel("output.xlsx", index=False)
	print("Excel file has been created successfully!")


if __name__ == "__main__":
	models = ["hermes-3-llama-3.2-3b"]
	urls = []
	with open ("links.txt", "r") as links_file:
		urls = links_file.read().splitlines()
	benchmark(models, urls)