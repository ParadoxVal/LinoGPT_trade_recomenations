import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv





# Load the .env file
load_dotenv()


import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

url = 'https://finance.yahoo.com/quote/TSLA/'

# Make a request to the website
r = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(r.content, 'html.parser')

text = soup.get_text()


# response = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#         {"role": "system", "content": "You are a helpful stock and cryto currency assistant. Respond with only Buy, Sell, or Hold based on the provided input. Then in the next line a short description of why you have decided that."},
#         {"role": "user", "content": f"Given the following text, recommend whether to buy, hold, or sell a stock: '{text}'.\n\nRecommendation:"}
#     ]
# )

# response['choices'][0]['message']['content']