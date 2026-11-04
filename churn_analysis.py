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

# 3. Exploratory Data Analysis & Visualizations
def plot_churn_insights(df):
    """
    Function to generate visualizations for Telecom Churn Analysis
    """
    plt.figure(figsize=(12, 5))
    
    # Plot 1: Churn Distribution
    if 'churn' in df.columns:
        plt.subplot(1, 2, 1)
        sns.countplot(data=df, x='churn', palette='Set2')
        plt.title('Customer Churn Distribution')
        plt.xlabel('Churn Status')
        plt.ylabel('Count')
        
    # Plot 2: Monthly Charges vs Churn
    if 'monthlycharges' in df.columns and 'churn' in df.columns:
        plt.subplot(1, 2, 2)
        sns.boxplot(data=df, x='churn', y='monthlycharges', palette='Set3')
        plt.title('Monthly Charges by Churn Status')
        plt.xlabel('Churn Status')
        plt.ylabel('Monthly Charges')
        
    plt.tight_layout()
    plt.show()

print("EDA Visualization Functions Added Successfully!")
