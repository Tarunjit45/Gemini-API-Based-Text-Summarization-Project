def split_text_into_chunks(text, chunk_size=1000):
    """
    Splits text into chunks of approximately `chunk_size` tokens.
    """
    words = text.split()
    chunks = [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

# Load the cleaned text
with open("cleaned_text.txt", "r", encoding="utf-8") as file:
    cleaned_text = file.read()

# Split the text into chunks
chunks = split_text_into_chunks(cleaned_text, chunk_size=1000)

# Save each chunk to a separate file (optional)
for idx, chunk in enumerate(chunks):
    with open(f"chunk_{idx + 1}.txt", "w", encoding="utf-8") as file:
        file.write(chunk)

print(f"Text segmentation complete! {len(chunks)} chunks created.")
