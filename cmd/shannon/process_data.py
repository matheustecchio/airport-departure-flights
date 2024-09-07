import numpy as np
import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta


def get_raw_data():
    data_path = Path("./data/shannon/raw_flights.csv")
    df = pd.read_csv(data_path)
    
    # Convert departure times to datetime format for better analysis
    df['Departure Time'] = pd.to_datetime(df['Departure Time'], format='%H:%M').dt.time

    return df

def join_minimum_capacity(df):
    # Define the minimum passenger capacities for each aircraft model
    minimum_passenger_capacities = {
        "B738": 162,
        "B38M": 178,
        "A20N": 140,
        "E190": 96,
        "A320": 150,
        "B737": 126,
        "B739": 178,
        "A321": 185,
        "A330": 250,
        "B77W": 368,
        "B789": 242,
        "A359": 300,
    }

    df['Minimum Passengers'] = df['Aircraft Model'].map(minimum_passenger_capacities)
    
    return df

def create_busy_times(df):
    # Function to create time ranges
    def generate_time_ranges(start_time, end_time, interval_minutes) -> list:
        time_ranges = []
        current_time = start_time
        while current_time < end_time:
            end_interval_time = current_time + timedelta(minutes=interval_minutes)
            time_ranges.append((current_time.time(), end_interval_time.time()))
            current_time += timedelta(minutes=interval_minutes)
        return time_ranges

    # Create the time ranges
    start_time = datetime.strptime('00:00', '%H:%M')
    end_time = datetime.strptime('23:59', '%H:%M')
    time_ranges = generate_time_ranges(start_time, end_time, 60)

    # Initialize lists to store results
    time_range_start = []
    time_range_end = []

    flight_count_list = []
    passenger_count_list = []

    # Process each time range
    for start, end in time_ranges:
        # Filter flights within the current time range
        flights_in_range = df[(df['Departure Time'] >= start) & (df['Departure Time'] < end)]
        
        # Count the number of flights
        flight_count = len(flights_in_range)
        
        # Sum the minimum passengers
        total_minimum_passengers = flights_in_range['Minimum Passengers'].sum()
        
        # Append results to lists
        time_range_start.append(f"{start.strftime('%H:%M')}")
        time_range_end.append(f"{end.strftime('%H:%M')}")
        flight_count_list.append(flight_count)
        passenger_count_list.append(total_minimum_passengers)

    # Create the resulting DataFrame
    busy_times_df = pd.DataFrame({
        'Start Time': time_range_start,
        'End Time': time_range_end,
        'Number of Flights': flight_count_list,
        'Minimum Passengers': passenger_count_list
    })

    return busy_times_df

def filter_if_no_flights(busy_times_df):
        # Filtering if time ranges has no flights
    busy_times_df = busy_times_df[busy_times_df['Number of Flights'] > 0]

    busy_times_df.reset_index(drop=True, inplace=True)

    return busy_times_df

def filter_tomorrow_flights(busy_times_df):
    # Filtering rows that are not within the current day
    # Get the current time in 'HH:MM' format
    time_now = datetime.now().strftime('%H:%M')

    # Initialize a list to store indices of rows to drop
    indices_to_drop = []

    # Iterate over the 'Time Range' column to check each time range
    for index, row in busy_times_df.iterrows():
        start_time = row["Start Time"]
        start_time = pd.to_datetime(start_time, format='%H:%M').strftime('%H:%M')
        
        if start_time > time_now:
            pass
        else:
            # Remove this rows
            indices_to_drop.append(index)

    # Drop the rows that are not within the desired time range
    busy_times_df = busy_times_df.drop(indices_to_drop)
    busy_times_df.reset_index(drop=True, inplace=True)

    return busy_times_df

def save(busy_times_df, df):
    # Saving everything
    busy_times_path = Path("./data/shannon/busy_times.csv")
    busy_times_df.to_csv(busy_times_path, index=False)

    flights_path = Path("./data/shannon/flights_processed.csv")
    df.to_csv(flights_path, index=False)

def process_data():
    # Load raw data
    df = get_raw_data()
    
    # Join with minimum capacity
    df = join_minimum_capacity(df)
    
    # Create busy times
    busy_times_df = create_busy_times(df)
    
    # Filter if no flights
    busy_times_df = filter_if_no_flights(busy_times_df)
    
    # Filter if flights are scheduled for tomorrow
    busy_times_df = filter_tomorrow_flights(busy_times_df)
    
    # Save everything
    save(busy_times_df, df)
    
    print("Data processing completed successfully!")
        
if __name__ == "__main__":
    process_data()