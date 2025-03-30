import pandas as pd

def read_csv_file(input_path):
    """Reads a CSV file and returns a DataFrame."""
    df = pd.read_csv(input_path)
    
    # Rename 'Unnamed: 0' to 'id' if it exists
    if "Unnamed: 0" in df.columns:
        df.rename(columns={"Unnamed: 0": "id"}, inplace=True)
    
    return df

def write_csv_file(df, output_path):
    """Writes a DataFrame to a CSV file."""
    df.to_csv(output_path, index=False)
    print(f"Data written to {output_path}")
