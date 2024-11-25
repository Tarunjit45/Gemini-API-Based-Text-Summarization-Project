import os
import time
import google.generativeai as genai
from dotenv import load_dotenv

API_KEY = 'AIzaSyAIlpBFW6jxDAjNw-kUJtLxmfpdnAx68lM'

# Configure the Gemini API client
genai.configure(api_key=API_KEY)
# Output directory to save responses
output_dir = "output_responses"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to process a single chunk
def process_chunk(chunk_filename):
    with open(chunk_filename, "r", encoding="utf-8") as file:
        text_chunk = file.read()

    # Generate content using the Gemini API
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(text_chunk)
    return response.text if response else "Error: No response received."

# Process each chunk file and add a delay
for i in range(1, 14):  # Adjust range if necessary
    chunk_filename = f"chunk_{i}.txt"
    if os.path.exists(chunk_filename):
        print(f"Processing {chunk_filename}...")
        try:
            # Process the chunk
            response_text = process_chunk(chunk_filename)
            
            # Save response
            output_filename = os.path.join(output_dir, f"response_{i}.txt")
            with open(output_filename, "w", encoding="utf-8") as output_file:
                output_file.write(response_text)
            print(f"Saved response for {chunk_filename}.")

        except Exception as e:
            print(f"Error processing {chunk_filename}: {e}")
        
        # Add a delay to avoid hitting API limits
        print("Waiting for 5 seconds to respect API rate limits...")
        time.sleep(5)  # Adjust delay as needed
    else:
        print(f"{chunk_filename} not found. Skipping...")

print("All chunks processed!")
