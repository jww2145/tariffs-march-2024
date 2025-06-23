import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Read processed exports and imports data
exports_path = 'processed_exports.csv'
imports_path = 'processed_imports.csv'

print("Reading processed data...")
exports = pd.read_csv(exports_path)
imports = pd.read_csv(imports_path)

# Display data info
print("\nExports data info:")
print(exports.info())
print("\nImports data info:")
print(imports.info())

# Calculate trade balance (exports - imports)
print("\nCalculating trade metrics...")

# Create a function to merge data and calculate metrics for each time period
def calculate_trade_metrics(exports_df, imports_df):
    # Ensure both dataframes have same structure before merging
    exports_df = exports_df[['Time', 'Date', 'Year', 'Month', 'Country', 'Value ($US)']]
    imports_df = imports_df[['Time', 'Date', 'Year', 'Month', 'Country', 'Value ($US)']]
    
    # Rename columns to distinguish exports and imports
    exports_df = exports_df.rename(columns={'Value ($US)': 'Exports'})
    imports_df = imports_df.rename(columns={'Value ($US)': 'Imports'})
    
    # Merge datasets on common fields
    merged = pd.merge(exports_df, imports_df, on=['Time', 'Date', 'Year', 'Month', 'Country'], how='outer')
    
    # Calculate trade metrics
    merged['Trade_Balance'] = merged['Exports'] - merged['Imports']
    merged['Trade_Volume'] = merged['Exports'] + merged['Imports']
    merged['Export_Import_Ratio'] = merged['Exports'] / merged['Imports']
    
    # Calculate Revealed Comparative Advantage Index (simplified version)
    # For detailed RCA, we would need product-level data
    merged['Export_Share'] = merged['Exports'] / merged.groupby('Time')['Exports'].transform('sum')
    merged['Import_Share'] = merged['Imports'] / merged.groupby('Time')['Imports'].transform('sum')
    merged['RCA_Index'] = merged['Export_Share'] / merged['Import_Share']
    
    return merged

# Calculate metrics
trade_metrics = calculate_trade_metrics(exports, imports)

# Display results
print("\nTrade metrics sample:")
print(trade_metrics.head())

# Save results
trade_metrics.to_csv('nafta_trade_metrics.csv', index=False)
print("\nTrade metrics saved to nafta_trade_metrics.csv")

# Create visualizations
print("\nGenerating visualizations...")

# Create a directory for plots if it doesn't exist
os.makedirs('plots', exist_ok=True)

# 1. Annual trade balance by country
annual_data = trade_metrics[trade_metrics['Month'] == 'Annual']
plt.figure(figsize=(12, 6))
for country in annual_data['Country'].unique():
    country_data = annual_data[annual_data['Country'] == country]
    plt.plot(country_data['Year'], country_data['Trade_Balance'] / 1e9, 
             marker='o', label=country)
plt.title('Annual Trade Balance by Country')
plt.xlabel('Year')
plt.ylabel('Trade Balance (Billion USD)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.savefig('plots/annual_trade_balance.png')

# 2. Export-Import Ratio over time
plt.figure(figsize=(12, 6))
for country in annual_data['Country'].unique():
    country_data = annual_data[annual_data['Country'] == country]
    plt.plot(country_data['Year'], country_data['Export_Import_Ratio'], 
             marker='o', label=country)
plt.axhline(y=1, color='r', linestyle='-', alpha=0.5, label='Balance point (Exports = Imports)')
plt.title('Export-Import Ratio by Country (Values > 1 indicate trade surplus)')
plt.xlabel('Year')
plt.ylabel('Export/Import Ratio')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.savefig('plots/export_import_ratio.png')

# 3. Revealed Comparative Advantage Index
plt.figure(figsize=(12, 6))
for country in annual_data['Country'].unique():
    country_data = annual_data[annual_data['Country'] == country]
    plt.plot(country_data['Year'], country_data['RCA_Index'], 
             marker='o', label=country)
plt.axhline(y=1, color='r', linestyle='-', alpha=0.5, label='Neutral advantage')
plt.title('Revealed Comparative Advantage Index by Country')
plt.xlabel('Year')
plt.ylabel('RCA Index (>1 indicates comparative advantage)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.savefig('plots/rca_index.png')

print("\nVisualizations saved to the 'plots' directory")
print("\nAnalysis complete!")
