import pandas as pd
import numpy as np

def clean_telecom_data(df):
    """
    Data Cleaning Pipeline for Telecom Churn Dataset
    """
    # 1. Standardize Column Names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    # 2. Convert Numeric Fields & Handle Missing Values
    if 'totalcharges' in df.columns:
        df['totalcharges'] = pd.to_numeric(df['totalcharges'], errors='coerce')
        df['totalcharges'] = df['totalcharges'].fillna(df['totalcharges'].median())
    
    # 3. Drop duplicate records if any
    df = df.drop_duplicates()
    
    print(f"Data Cleaning Completed. Final Shape: {df.shape}")
    return df

if __name__ == "__main__":
    print("Telecom Data Processing Pipeline Initialized...")
