import pandas as pd
import glob

# Step 1: Find all CSV files in the current working directory
csv_files = glob.glob('*.csv')  # This will find all CSV files in the current folder

# Check that CSV files are found
print(f"CSV files found: {csv_files}")

import pandas as pd
import glob

# Step 1: Find all CSV files in the current working directory
csv_files = glob.glob('*.csv')  # or 'sample_data/*.csv' if inside a folder

# Step 2: Read all CSV files into DataFrames and combine them
dfs = [pd.read_csv(file) for file in csv_files]
all_data = pd.concat(dfs, ignore_index=True)

# Step 3: Reshape the data so that each row is a station-month-temperature entry
melted = pd.melt(all_data, id_vars=['STN_ID'], 
                 value_vars=['January', 'February', 'March', 'April', 'May', 'June', 
                             'July', 'August', 'September', 'October', 'November', 'December'], 
                 var_name='month', value_name='temperature')

# Step 4: Map each month to a season in Australia
month_to_season = {
    'January': 'Summer', 'February': 'Summer', 'December': 'Summer',
    'March': 'Autumn', 'April': 'Autumn', 'May': 'Autumn',
    'June': 'Winter', 'July': 'Winter', 'August': 'Winter',
    'September': 'Spring', 'October': 'Spring', 'November': 'Spring'
}
melted['season'] = melted['month'].map(month_to_season)

# Step 5: Calculate average temperature for each season
seasonal_averages = melted.groupby('season')['temperature'].mean()

# Step 6: Save seasonal averages in specific order
with open('average_temp.txt', 'w') as f:
    for season in ['Summer', 'Autumn', 'Winter', 'Spring']:
        avg_temp = seasonal_averages[season]
        f.write(f"{season}: {avg_temp:.2f}\n")

# Step 7: Calculate temperature range for each station
station_ranges = melted.groupby('STN_ID')['temperature'].agg(['max', 'min'])
station_ranges['range'] = station_ranges['max'] - station_ranges['min']

# Step 8: Identify the station(s) with the largest temperature range
max_range = station_ranges['range'].max()
largest_range_stations = station_ranges[station_ranges['range'] == max_range].index.tolist()

# Step 9: Output the station(s)
print("Stations with the largest temperature range:", largest_range_stations)

