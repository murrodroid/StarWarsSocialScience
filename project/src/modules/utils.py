import pandas as pd

def read_csv_file(file_path):
    try:
        df = pd.read_csv(file_path,sep=";")
        return df
    except Exception as e:
        print(f"Failed to read CSV: {e}")
        return None