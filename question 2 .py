import pandas as pd
import glob

# import list of CSV files 
csv_files = glob.glob('temperature_data/*.csv')

# Read and merge all CSV files into a single DataFrame
dfs = [pd.read_csv(file) for file in csv_files]
all_data = pd.concat(dfs, ignore_index=True)

#  Transform monthly columns into rows
melted = pd.melt(all_data, id_vars=['STN_ID'], 
                 value_vars=['January', 'February', 'March', 'April', 'May', 'June', 
                             'July', 'August', 'September', 'October', 'November', 'December'], 
                 var_name='month', value_name='temperature')

# Define month-to-season mapping 
month_to_season = {
    'January': 'Summer', 'February': 'Summer', 'December': 'Summer',
    'March': 'Autumn', 'April': 'Autumn', 'May': 'Autumn',
    'June': 'Winter', 'July': 'Winter', 'August': 'Winter',
    'September': 'Spring', 'October': 'Spring', 'November': 'Spring'
}

# Add a season column based on the month
melted['season'] = melted['month'].map(month_to_season)

# Calculate average temperature for each season across all years and stations
seasonal_averages = melted.groupby('season')['temperature'].mean()

# Save seasonal averages to "average_temp.txt" in specified order
with open('average_temp.txt', 'w') as f:
    for season in ['Summer', 'Autumn', 'Winter', 'Spring']:
        avg_temp = seasonal_averages[season]
        f.write(f"{season}: {avg_temp:.2f}\n")

# Calculate the temperature range for each station
station_ranges = melted.groupby('STN_ID')['temperature'].agg(['max', 'min'])
station_ranges['range'] = station_ranges['max'] - station_ranges['min']
max_range = station_ranges['range'].max()
largest_range_stations = station_ranges[station_ranges['range'] == max_range].index.tolist()

#  station(s) with the largest temperature range to "largest_temp_range_station.txt"
with open('largest_temp_range_station.txt', 'w') as f:
    for station in largest_range_stations:
        f.write(f"{station}\n")

# Calculate the average temperature for each station
station_averages = melted.groupby('STN_ID')['temperature'].mean()
warmest_avg = station_averages.max()
coolest_avg = station_averages.min()
warmest_stations = station_averages[station_averages == warmest_avg].index.tolist()
coolest_stations = station_averages[station_averages == coolest_avg].index.tolist()

#  warmest and coolest stations to "warmest_and_coolest_station.txt"
with open('warmest_and_coolest_station.txt', 'w') as f:
    f.write("Warmest stations:\n")
    for station in warmest_stations:
        f.write(f"{station}\n")
    f.write("\nCoolest stations:\n")
    for station in coolest_stations:
        f.write(f"{station}\n")
