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



