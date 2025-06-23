import pandas as pd
import numpy as np
import os

# Set path for input and output
input_path = 'csv files/Standard Report - Imports.csv'
output_path = 'processed_imports.csv'

# Read the CSV file
print("Reading imports data...")
imports = pd.read_csv(input_path)

# Display original data info
print("\nOriginal data info:")
print(imports.info())
print("\nOriginal data sample:")
print(imports.head())

# Drop the unnamed column if it exists
if 'Unnamed: 3' in imports.columns:
    imports = imports.drop('Unnamed: 3', axis=1)
    print("\nDropped 'Unnamed: 3' column")

# Rename the value column to match exports for easier merging
imports.rename(columns={'Customs Value (Gen) ($US)': 'Value ($US)'}, inplace=True)

# Clean the Value column: remove commas and convert to float
print("\nCleaning Value column...")
imports['Value ($US)'] = imports['Value ($US)'].str.replace(',','').astype(float)

# Create Year and Month columns for better analysis
imports['Year'] = imports['Time'].str.extract(r'(\d{4})').fillna(imports['Time'])
imports['Month'] = imports['Time'].str.extract(r'(\w+)\s+\d{4}').fillna('Annual')

# Extract month number for better sorting
month_map = {
    'January': '01', 'February': '02', 'March': '03', 'April': '04',
    'May': '05', 'June': '06', 'July': '07', 'August': '08',
    'September': '09', 'October': '10', 'November': '11', 'December': '12',
    'Annual': '00'  # Special case for annual data
}
imports['Month_Num'] = imports['Month'].map(month_map)

# Create a proper date column for time series analysis
imports['Date'] = np.where(
    imports['Month'] == 'Annual',
    imports['Year'],  # Use just the year for annual values
    imports['Year'] + '-' + imports['Month_Num'] + '-01'  # Create a date at the start of the month
)

# Reorder columns in a logical way
column_order = ['Time', 'Date', 'Year', 'Month', 'Month_Num', 'Country', 'Value ($US)']
imports = imports[column_order]

# Display cleaned data
print("\nCleaned data info:")
print(imports.info())
print("\nCleaned data sample:")
print(imports.head())

# Save the processed data
imports.to_csv(output_path, index=False)
print(f"\nProcessed data saved to {output_path}")
