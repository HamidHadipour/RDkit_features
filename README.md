# SMILES Feature Extraction
This Python script processes SMILES (Simplified Molecular Input Line Entry System) strings to extract molecular features using the Morgan descriptor, a method commonly used in cheminformatics for generating molecular fingerprints. The script is designed to handle large datasets, apply normalization techniques, and manage missing values, making it suitable for preparing molecular datasets for machine learning and data analysis tasks.

# Features
Molecular Feature Extraction: Extract features from SMILES strings using the Morgan descriptor.
Normalization: Support for different normalization techniques to scale the features.
Missing Value Management: Options to handle missing values by either filling them with the column mean or leaving them as is.
Flexible Output Formats: Save the processed data in either CSV or Parquet format.
Requirements<br>
<li>
Python 3.6 or higher
Pandas
NumPy
scikit-learn
descriptastorus
Installation
</li>
