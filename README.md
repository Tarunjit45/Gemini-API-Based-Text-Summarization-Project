# Gemini API-Based Text Summarization Project

## Overview
This project demonstrates the use of Google's Generative AI, **Gemini API**, to process large chunks of text and generate concise summaries. The workflow involves segmenting a large text, processing it with the Gemini API, and combining the results into a comprehensive summary. This project was submitted as part of a Kaggle competition focused on utilizing AI for long-context window processing.

---

## Features
- **Text Segmentation**: Automatically splits large input text into manageable chunks.
- **API Integration**: Uses the Gemini API to generate contextually relevant summaries for each text chunk.
- **Data Pipeline**: Seamlessly combines responses into a unified output.
- **Reproducible Workflow**: Includes scripts for preprocessing, processing, and postprocessing.
- **Kaggle Dataset and Notebook**: Uploaded processed files and documented the workflow for community sharing.

---

## Workflow
### 1. **Data Preparation**
   - Extract raw text from a PDF file.
   - Clean the text by removing unwanted characters or formatting.
   - Segment the cleaned text into smaller chunks.

### 2. **Processing with Gemini API**
   - Configure the Gemini API with an API key.
   - Process each chunk individually using the API to generate summaries.

### 3. **Post-Processing**
   - Combine the individual responses into a single summarized document.
   - Extract key insights and trends for analysis.

### 4. **Dataset and Notebook Creation**
   - Upload processed files as a Kaggle dataset.
   - Document the workflow in a Kaggle notebook with code and insights.

---

## Project Structure
```plaintext
project/
│
├── data/
│   ├── chunk_1.txt
│   ├── chunk_2.txt
│   ├── ... (other chunk files)
│   └── final_combined_output.txt
│
├── scripts/
│   ├── extract_text.py
│   ├── clean_text.py
│   ├── segment_text.py
│   ├── process_all_chunks.py
│   └── combine_responses.py
│
├── kaggle_notebook/
│   ├── gemini_text_summarization.ipynb
│
├── .env               # Environment variables
├── README.md          # This file
└── requirements.txt   # Python dependencies

```
---

## Setup Instructions

### Prerequisites
1. Python 3.8 or higher.
2. A Google Gemini API key.
3. A Kaggle account for uploading datasets and notebooks.

### Installation Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/gemini-text-summarization.git
   cd gemini-text-summarization
2. **Set up a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate   # On Linux/macOS
    env\Scripts\activate      # On Windows
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Configure API Key:**
   ```bash
   GEMINI_API_KEY=your_api_key_here
5. **Run Scripts in Sequence:**
   ```bash
   Extract text from a PDF:
    python scripts/extract_text.py
Clean the text:

    python scripts/clean_text.py
Segment the cleaned text:

    python scripts/segment_text.py
Process text chunks with the Gemini API:

    python scripts/process_all_chunks.py
Combine the responses:

    python scripts/combine_responses.py
       
MIT License

Copyright (c) 2024 Tarunjit Biswas

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

