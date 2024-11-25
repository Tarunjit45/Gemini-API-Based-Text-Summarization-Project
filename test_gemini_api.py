import os
import google.generativeai as genai
from dotenv import load_dotenv

API_KEY = 'AIzaSyAIlpBFW6jxDAjNw-kUJtLxmfpdnAx68lM'

# Configure the Gemini API client
genai.configure(api_key=API_KEY)

# Read a text chunk
with open("chunk_1.txt", "r", encoding="utf-8") as file:
    text_chunk = file.read()

# Specify the model for the API request (gemini-1.5-pro-latest)
model = genai.GenerativeModel('gemini-1.5-pro-latest')

# Send the request to generate content using the model
response = model.generate_content(text_chunk)

# Check if the response is successful
if response:
    output_text = response.text
    print("Response received:\n", output_text)
else:
    print("Error: Failed to receive response.")
