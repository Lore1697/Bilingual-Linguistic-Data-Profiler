# Bilingual Linguistic Data Profiler

A Python-based tool for profiling bilingual Italian–English text datasets using basic NLP and linguistic statistics.

---

## Overview

This project analyzes text data and extracts key linguistic features such as:

- Language detection (Italian vs English)
- Word statistics
- Lexical diversity
- Most frequent content words
- Dataset-level comparisons between languages

It also includes a simple Streamlit interface for analyzing text interactively.

---

## Use Cases

This project is relevant for roles involving:

- AI data annotation
- Language data analysis
- Content quality evaluation
- NLP-oriented data processing
- Bilingual text analysis

---

## Features

- Load text data from a CSV file
- Clean and tokenize text
- Detect language using rule-based markers
- Remove basic stopwords in Italian and English
- Compute:
  - Word count
  - Unique word count
  - Lexical diversity
  - Most frequent words
- Compare Italian and English texts at dataset level
- Export structured results to a CSV report
- Analyze custom text through a Streamlit web app

---

## Project Structure

```text
bilingual-linguistic-data-profiler/
│
├── data/
│   └── sample_texts.csv
│
├── app.py
├── linguistic_profiler.py
├── linguistic_report.csv
└── README.md
```

---

## Example Output

```text
--- DATASET SUMMARY ---
Total texts: 8
Italian texts: 4
English texts: 4
Average lexical diversity: 0.99
Top words overall: [('data', 3), ('artificiale', 2), ('text', 2), ('python', 2)]

--- LANGUAGE COMPARISON ---
English:
  Texts: 4
  Average word count: 8.25
  Average lexical diversity: 1.0

Italian:
  Texts: 4
  Average word count: 9.25
  Average lexical diversity: 0.98
```

---

## How to Run

Run the command-line profiler:

```bash
python linguistic_profiler.py
```

The script reads input from:

```text
data/sample_texts.csv
```

and generates:

```text
linguistic_report.csv
```

---

## Streamlit App

The project also includes a simple Streamlit interface for interactive text analysis.

Run it with:

```bash
python -m streamlit run app.py
```

The app allows users to enter custom Italian or English text and view linguistic statistics directly in the browser.

---

## Technologies

- Python
- CSV
- Regular Expressions
- Collections / Counter
- Pandas
- Streamlit
- Rule-based NLP

---

## Limitations

- Rule-based approach, no machine learning models
- Language detection is heuristic and simplified
- Designed for demonstration, not production use
- Works best with short Italian and English text samples

---

## Future Improvements

- Expand dataset size
- Improve language detection
- Add sentence-level analysis
- Add readability metrics
- Support additional languages
- Export Markdown or HTML reports
- Improve dashboard visualizations

---

## Author

Lorenzo Guerrieri
