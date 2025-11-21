# CyberAIBenchmark

## Description
CyberAIBenchmark is a Python-based cybersecurity benchmarking tool designed to evaluate AI models by scraping content from specified web pages and sending it to language models for processing. The results are then saved in an Excel file for analysis. This tool helps compare the performance of different AI models on structured web-based data.

## Features
- Scrapes structured content from specified URLs.
- Sends the extracted data as input to AI language models.
- Collects AI-generated responses and compiles them into an Excel file.
- Supports multiple AI models for benchmarking.
- Evaluates AI model responses against reference solutions using a predefined grading rubric.
- Supports custom challenges via JSON file alongside scraped content.
- Option to run evaluation separately from benchmarking.

## Dependencies
Ensure you have the following dependencies installed before running the script:

```bash
pip install -r requirements
```

## Usage

### 1. Prepare the Input URLs
Create a file named `links.txt` and `models.txt` in the same directory as the script, or provide the path to them in the arguments. Add the URLs you want to scrape, one per line (PortSwigger and PentesterLab links only) inside the links text file and the id of the models you want to test them against in the models text file, one per line also.

### 2. Open Local LLM processing server
Open the local llm processing server with the models you want. It's best to use "LMStudio" to make the server as they have a JIT Model Loader to change model on the fly. The program will send chat completions requests using the OpenAI API format.

### 3. Run the Script
Execute the Python script to start the benchmarking process with the following command:

```bash
python benchmark.py -m .\path\to\models.txt -l .\path\to\links.txt -llm_prompt_url http://127.0.0.1:1234/v1/chat/completions -llm_get_models_url http://localhost:1234/api/v0/models/ -preload -o output
```

#### Additional Options:
- **Evaluation**: Add `-evaluate` to evaluate model responses against reference solutions:
  ```bash
  python benchmark.py -m .\models.txt -l .\links.txt -evaluate
  ```

- **Custom Challenges**: Use `-custom_challenges` to include your own challenges:
  ```bash
  python benchmark.py -m .\models.txt -l .\links.txt -custom_challenges .\custom_challenges.json
  ```

- **Evaluation Only**: Use `-no_benchmark -evaluate` to run only the evaluation on existing results:
  ```bash
  python benchmark.py -m .\models.txt -no_benchmark -evaluate -evaluation_input .\output\benchmarking_output.xlsx
  ```

### 4. Output
- The script will scrape content from the URLs listed in `.\links.txt` by default.
- It will send the extracted content to the specified AI models in `.\models.txt` by default.
- The LLM default endpoint url is `http://127.0.0.1:1234/v1/chat/completions`.
- The responses will be saved in `output.xlsx` by default.
- If evaluation is enabled, evaluation results will be saved in `evaluation_output.xlsx`.
- A confirmation message will be displayed upon successful completion.

## Configuration
- **Models**: You can specify the AI models to be tested in the `models` text file.
- **LLM API URL**: Modify the `llm_url` parameter to point to the correct API endpoint.
- **Custom Challenges**: Create a JSON file with your own challenges following the format in `custom_challenges.json`.
- **Evaluation Input**: Specify an existing benchmark output file for evaluation with the `-evaluation_input` parameter.
- **No Benchmark**: Use `-no_benchmark` to skip the benchmarking process and only run evaluation.

## Code Structure
- `scrape_info(url)`: Extracts structured content from a given URL.
- `send_benchmarking_prompt(prompt, model, llm_url)`: Sends a benchmarking prompt request to an AI model and retrieves its answer.
- `send_evaluation_prompt(solution, llm_response, model, llm_url)`: Sends an evaluation prompt request to evaluate an AI model's response against a reference solution.
- `load_model(model, llm_prompt_url, llm_get_models_url)`: Sends a request to the llm server to force load a model (only works if you're using a JIT Model Loader).
- `benchmark(preload_model, models, urls, llm_prompt_url, llm_get_models_url, output, do_evaluate, custom_challenges)`: Orchestrates the benchmarking process, storing results in an Excel file and optionally running evaluation.
- `evaluate(preload_model, models, llm_prompt_url, llm_get_models_url, input, output)`: Evaluates AI model responses against reference solutions, storing results in an Excel file.
- `main`: Reads URLs from `links.txt`, defines models from `models.txt`, loads custom challenges if specified, and calls `benchmark()` and/or `evaluate()`.

## Notes
- The script assumes a running AI model server at `http://127.0.0.1:1234/v1/chat/completions`.
- Modify the script as needed to fit different model endpoints or scraping structures.
- Ensure URLs in `links.txt` contain structured data relevant to benchmarking.

## License
This project is open-source. Feel free to modify and distribute as needed.
