# SMILES Feature Extraction

This Python script processes SMILES (Simplified Molecular Input Line Entry System) strings to extract molecular features using the Morgan descriptor. It is designed for cheminformatics applications, particularly in preparing molecular datasets for machine learning and data analysis tasks.

## Features

- **Molecular Feature Extraction**: Extracts features from SMILES strings using the Morgan descriptor method.
- **Normalization Options**: Supports various normalization techniques, including cumulative distribution function, min-max scaling, and standard scaling.
- **Missing Value Management**: Offers options to handle missing values by either filling them with the column mean or leaving them as is.
- **Output Flexibility**: Allows saving the processed data in either CSV or Parquet formats.

## Requirements

The script requires the following environment and libraries:

- Python 3.6 or higher
- Pandas
- NumPy
- scikit-learn
- descriptastorus

## Installation

To get started with this script, clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/smiles-feature-extraction.git
cd smiles-feature-extraction
pip install -r requirements.txt
