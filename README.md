# Data Automation Pipeline with Python

This project automates data ingestion, cleaning, transformation, and visualization using Python. It is designed to handle large datasets (150,000+ rows), reduce manual workload, and provide clean, visualized insights in a reusable and scalable way.


## Project Overview

- Load large CSV datasets efficiently using Pandas
- Clean missing values, remove duplicates, and normalize column names
- Transform data with additional logic (e.g., experience level classification)
- Visualize data distributions with Matplotlib
- Modular script structure for reusability

---

## Key Features

- Automated pipeline : One script to run all steps (ETL + visualization)
- Handles large files : Optimized for 150k+ row datasets
- Clear output : Saves both cleaned CSV and bar chart as image
- Beginner-friendly : Easy to understand, extend, and deploy

---

## Tech Stack

- Python 3.10+
- Pandas
- Matplotlib

---

## Folder Structure

data_automation_project/
├── data/
│ ├── raw_data.csv # Input file (your dataset)
│ ├── cleaned_data.csv # Output after processing
│ └── plot.png # Output plot
│
├── scripts/
│ ├── ingest_data.py # Ingests CSV data
│ ├── clean_data.py # Cleans raw data
│ ├── transform_data.py # Adds transformations
│ └── visualize_data.py # Generates plots
│
├── pipeline_runner.py # Main file to run entire pipeline
├── requirements.txt # Python dependencies
└── README.md # Project overview


---

## How to Run the Project

### 1. Clone the Repository

git clone https://github.com/<kaviyavarshini-CS>/data-automation-pipeline.git
cd data-automation-pipeline

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Add Dataset

Download and place your CSV file as:
data/raw_data.csv

Or generate a sample dataset using:

python scripts/generate_sample_data.py

### 4. Run the Pipeline

python pipeline_runner.py

### 5. Output

data/cleaned_data.csv
data/plot.png — a bar chart of department distribution

### Example Output

Chart will be saved and displayed at the end of the pipeline.

Department Distribution:
--------------------------------
engineering | █████████████
hr          | ██████
marketing   | ████
finance     | ███
