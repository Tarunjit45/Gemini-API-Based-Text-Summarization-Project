from PyPDF2 import PdfReader

# Path to your PDF file
pdf_path = "2411.13960v1.pdf"

# Initialize the PDF reader
reader = PdfReader(pdf_path)

# Extract text from each page
full_text = ""
for page in reader.pages:
    full_text += page.extract_text()

# Save the extracted text to a file
with open("extracted_text.txt", "w", encoding="utf-8") as text_file:
    text_file.write(full_text)

print("Text extraction complete! Check 'extracted_text.txt'")
