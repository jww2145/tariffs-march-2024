import pandas as pd
import numpy as np
import os

# Set path for input and output
input_path = 'csv files/Standard Report - Exports.csv'
output_path = 'processed_exports.csv'

# Read the CSV file
print("Reading exports data...")
exports = pd.read_csv(input_path)

# Display original data info
print("\nOriginal data info:")
print(exports.info())
print("\nOriginal data sample:")
print(exports.head())

# Clean the Value column: remove commas and convert to float
print("\nCleaning Value column...")
exports['Value ($US)'] = exports['Value ($US)'].str.replace(',','').astype(float)

# Create Year and Month columns for better analysis
exports['Year'] = exports['Time'].str.extract(r'(\d{4})').fillna(exports['Time'])
exports['Month'] = exports['Time'].str.extract(r'(\w+)\s+\d{4}').fillna('Annual')

# Keep the original Time column but also create separate columns for analytical purposes
# Extract month number for better sorting
month_map = {
    'January': '01', 'February': '02', 'March': '03', 'April': '04',
    'May': '05', 'June': '06', 'July': '07', 'August': '08',
    'September': '09', 'October': '10', 'November': '11', 'December': '12',
    'Annual': '00'  # Special case for annual data
}
exports['Month_Num'] = exports['Month'].map(month_map)

# Create a proper date column for time series analysis
exports['Date'] = np.where(
    exports['Month'] == 'Annual',
    exports['Year'],  # Use just the year for annual values
    exports['Year'] + '-' + exports['Month_Num'] + '-01'  # Create a date at the start of the month
)

# Reorder columns in a logical way
column_order = ['Time', 'Date', 'Year', 'Month', 'Month_Num', 'Country', 'Value ($US)']
exports = exports[column_order]

# Display cleaned data
print("\nCleaned data info:")
print(exports.info())
print("\nCleaned data sample:")
print(exports.head())

# Save the processed data
exports.to_csv(output_path, index=False)
print(f"\nProcessed data saved to {output_path}")
