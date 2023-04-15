# Stock and Cryptocurrency Assistant

This is a Python project that helps users to decide whether to buy, sell or hold a stock based on a provided input.

### Setup

1. Clone the repository.
2. Install the required packages: pip install -r requirements.txt
3. Obtain an OpenAI API key and create a .env file in the root directory with the following content:
4. Obtain a Google service account 

```
OPENAI_API_KEY=<your_api_key>
Run the main.py file: python scrape.py.
```

### Usage
The program will scrape financial news data from Yahoo Finance and prompt the user to decide whether to buy, sell, or hold a stock. The user will be asked to provide a short description of the reason behind the decision.

The program will use OpenAI's GPT-3.5-turbo model to generate a response based on the user's input and provide a recommendation.

.gitignore
The .gitignore file has been set up to ignore the .env file so that the API key is not exposed on GitHub.