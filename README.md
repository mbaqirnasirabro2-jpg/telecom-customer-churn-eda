import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for visuals
sns.set_theme(style="whitegrid")

def load_and_clean_data(file_path):
    """
    Function to load, clean and preprocess Telecom Churn Dataset.
    """
    # 1. Load Data
    df = pd.read_csv(file_path)
    print(f"Dataset Shape: {df.shape}")
    
    # 2. Handle Missing Values
    # TotalCharges is often stored as object due to blank spaces
    if 'TotalCharges' in df.columns:
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
        # Fill missing values with median
        df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)
    
    # Clean column names (strip whitespace and lower case)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    print("Data Cleaning Completed. Missing Values Handled.")
    return df

def generate_eda_insights(df):
    """
    Generate key Exploratory Data Analysis metrics.
    """
    print("\n--- DATA INSIGHTS ---")
    if 'churn' in df.columns:
        churn_rate = df['churn'].value_counts(normalize=True) * 100
        print(f"Overall Churn Rate:\n{churn_rate}\n")
    
    # Statistical Summary for Numeric Features
    print("Numerical Summary:")
    print(df.describe().T)

if __name__ == "__main__":
    # Sample execution pipeline structure
    print("Data Processing & EDA Pipeline Initialized...")
