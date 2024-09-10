import pandas as pd
from descriptastorus.descriptors.DescriptorGenerator import MakeGenerator
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import argparse
import sys

# Initialize RDKit 2D feature generator
generator = MakeGenerator(("RDKit2D",))

def extract_features(smiles):
    """
    Function to extract RDKit features from a SMILES string.
    Returns a list of features or None if the SMILES is invalid.
    """
    try:
        data = generator.process(smiles)
        if data[0]:  # Check if the SMILES was valid and processed
            return data[1:]
        else:
            return None  # Return None if SMILES could not be processed
    except:
        return None

def normalize_features(features_df, method):
    """
    Normalize features using the specified method.
    """
    if method == 'CDF':
        return features_df.rank(method='average', pct=True)
    elif method == 'minmax':
        scaler = MinMaxScaler()
        return pd.DataFrame(scaler.fit_transform(features_df), columns=features_df.columns)
    elif method == 'standardscaler':
        scaler = StandardScaler()
        return pd.DataFrame(scaler.fit_transform(features_df), columns=features_df.columns)
    return features_df

def handle_missing_values(features_df, fill_nan):
    """
    Handle missing values in the features DataFrame.
    Inform the user about the presence of NaNs, and decide whether to fill them based on user input.
    """
    if features_df.isnull().any().any():  # Check if any NaN values are present
        print("There are missing (NaN) values in the data.")
        if fill_nan:
            print("Filling missing values with the mean of each column...")
            features_df = features_df.fillna(features_df.mean())
        else:
            print("Leaving the missing values as they are.")
    else:
        print("There are no missing values in the data.")
    
    return features_df

def process_smiles_dataframe(input_path, output_type, output_file, normalization, fill_nan):
    """
    Load, process, and save a DataFrame containing SMILES strings.
    """
    print(f"Loading data from {input_path}...")
    if not input_path.endswith('.csv'):
        raise ValueError("Input file must be a CSV.")

    df = pd.read_csv(input_path)
    
    if 'SMILES' not in df.columns:
        raise ValueError("The input CSV does not contain a 'SMILES' column.")
    
    if df['SMILES'].isnull().any():
        raise ValueError("There are empty entries in the 'SMILES' column.")

    print("Extracting features from SMILES data...")
    features = df['SMILES'].apply(extract_features)
    column_names = [name for name, dtype in generator.GetColumns()[1:]]
    features_df = pd.DataFrame(features.tolist(), columns=column_names)

    features_df = handle_missing_values(features_df, fill_nan)

    if normalization and normalization != 'False':
        print(f"Applying {normalization} normalization...")
        features_df = normalize_features(features_df, normalization)

    print(f"Saving the processed data to {output_file}.{output_type}...")
    if output_type == 'csv':
        features_df.to_csv(f"{output_file}.csv", index=False)
    elif output_type == 'parquet':
        features_df.to_parquet(f"{output_file}.parquet")
    else:
        raise ValueError("Unsupported output type. Choose 'csv' or 'parquet'.")

def main():
    parser = argparse.ArgumentParser(description='Process SMILES strings and extract features.')
    parser.add_argument('--input', required=True, help='Input CSV file path.')
    parser.add_argument('--output_type', choices=['csv', 'parquet'], required=True, help='Output file type (csv or parquet).')
    parser.add_argument('--output_file', required=True, help='Output file name.')
    parser.add_argument('--normalization', choices=['False', 'CDF', 'minmax', 'standardscaler'], default='False', help='Normalization method to apply.')
    parser.add_argument('--fill_nan', type=bool, default=False, help='Fill missing values with average (True/False).')

    args = parser.parse_args()

    process_smiles_dataframe(args.input, args.output_type, args.output_file, args.normalization, args.fill_nan)

if __name__ == "__main__":
    main()
