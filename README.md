# Song Popularity Prediction

This project aims to predict the popularity of songs using various features from Spotify and Billboard data.

## Project Structure

The project is organized as follows:

```plaintext
song-popularity-prediction/
├── data/                   # Data storage
│   ├── raw/                # Raw data from APIs
│   ├── processed/          # Processed data for modeling
│   └── external/           # External datasets
├── notebooks/              # Jupyter notebooks for EDA and prototyping
├── src/                    # Source code for the project
│   ├── __init__.py
│   ├── data_collection.py  # Scripts for data extraction
│   ├── data_preprocessing.py  # Scripts for data preprocessing
│   ├── model_training.py   # Scripts for model training
│   ├── model_evaluation.py # Scripts for model evaluation
│   └── visualization.py    # Scripts for data visualization
├── environment.yml         # Conda environment setup
├── requirements.txt        # pip requirements
├── .gitignore              # Git ignore file
├── README.md               # Project description and instructions
└── ETL_pipeline.py         # Main ETL pipeline script
