Take raw API responses and transform them into clean, human-readable tables with Python + Pandas.
Built in Jupyter to support prompt engineering and LLM training workflows by making complex data easy to interpret and structure.

# 🧩 API Response Breakdown for Prompt Engineering

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)  
[![Jupyter](https://img.shields.io/badge/Environment-Jupyter%20Notebook-orange.svg)](https://jupyter.org/)  
[![Pandas](https://img.shields.io/badge/Library-Pandas-green.svg)](https://pandas.pydata.org/)  

## 📌 Overview
This project demonstrates how to take a raw **API response** and transform it into a clear, structured, and **easy-to-read format**.  

The goal is to **support prompt engineering workflows** for **LLM (Large Language Model) training**, making it easier to extract insights and design effective prompts.  

## ⚙️ Tech Stack
- **Languages:** Python, Markdown  
- **Environment:** Jupyter Notebook  
- **Libraries/Tools:** Pandas  

## 🚀 Features
- Fetch and parse JSON-based API responses  
- Convert complex nested data into tabular structures  
- Clean and format data using **Pandas**  
- Present results in Markdown-friendly tables for readability  
- Provide a foundation for **LLM training and prompt engineering**  

## 📂 Repository Structure

new_api_tutorial
  ├── notebooks/ # Jupyter notebooks with step-by-step examples  
  ├── data/ # Example API responses (JSON/CSV)  
  ├── utils/ # Helper scripts for parsing/formatting  
  ├── README.md # Project documentation  
  └── requirements.txt # Python dependencies  
  
## 🔧 Installaing & Setting Up Inside Your Terminal
1. Clone the repository:
   ```bash
   git clone https://github.com/npj210mlk/new_api_tutorial.git
   cd new_api_tutorial

2. In case you want to create and activate a virtual environment (recommended)

    python3 -m venv venv
    source venv/bin/activate   # if you're using macOS/Linux
    venv\Scripts\activate      # if you're using Windows

3. Install the stuff you need
    pip install -r requirements.txt

4. Launch Jupyter Notebook from this repository
    jupyter notebook


## 📖 Usage
Open the notebook in the notebooks/ directory

Run the cells step-by-step to:

Fetch an API response

Parse JSON into Python objects

Transform into Pandas DataFrames

Display results in a clean, tabular format

This provides an LLM-friendly dataset for testing prompt structures and building AI workflows.

## 🌟 Example Output
How the API Responds (Truncated):
{
  "user": {
    "id": 123,
    "name": "Alice",
    "roles": ["admin", "editor"]
  },
  "status": "active"
}

How You See It:
| id  | name  | roles               | status |
| --- | ----- | ------------------- | ------ |
| 123 | Alice | \['admin','editor'] | active |

## 🎯 Purpose

Designed to bridge data engineering and prompt engineering, this repo helps streamline the messy process of turning API data into LLM-training-ready formats.

## 🤝 Contributing

Contributions are welcome! If you’d like to extend this project (e.g., add new parsers, handle more APIs), feel free to fork the repo and submit a PR.

## 📜 License
This project is licensed under the MIT License. See [LICENSE](https://en.wikipedia.org/wiki/MIT_License) for details.
