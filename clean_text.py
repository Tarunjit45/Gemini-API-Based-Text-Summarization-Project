import re

# Path to your extracted text file
input_file = "extracted_text.txt"
output_file = "cleaned_text.txt"

# Read the extracted text
with open(input_file, "r", encoding="utf-8") as file:
    text = file.read()

# Clean the text
# Remove multiple line breaks
cleaned_text = re.sub(r"\n\s*\n", "\n", text)

# Remove page numbers (e.g., "Page 1")
cleaned_text = re.sub(r"Page \d+", "", cleaned_text)

# Remove any extra spaces
cleaned_text = re.sub(r"[ \t]+", " ", cleaned_text)

# Write the cleaned text to a new file
with open(output_file, "w", encoding="utf-8") as file:
    file.write(cleaned_text)

print("Text cleaning complete! Check 'cleaned_text.txt'")
