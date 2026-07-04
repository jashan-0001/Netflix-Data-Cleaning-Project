# Netflix Data Cleaning Project

## Project Overview

This project cleans the Netflix Movies and TV Shows dataset using Python and Pandas.

## Dataset

- Original Dataset: data/netflix_movies1.csv
- Cleaned Dataset: data/Netflix_Final_Cleaned.csv

## Cleaning Steps

- Removed duplicate records
- Standardized column names
- Removed extra spaces
- Handled missing values
- Converted dates into standard format
- Created Year Added column
- Created Content Age column
- Renamed Listed In to Genre
- Sorted dataset alphabetically

## Technologies Used

- Python
- Pandas
- VS Code

## Project Structure

```
Netflix-Data-Cleaning-Project
│
├── data
├── scripts
├── images
├── README.md
├── requirements.txt
└── .gitignore
```

## How to Run

```bash
pip install -r requirements.txt
python scripts/clean_netflix_data.py
```

## Author

Jashanpreet Singh
