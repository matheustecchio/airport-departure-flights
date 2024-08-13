import pandas as pd
from pathlib import Path
import shutil

def read_csv():
    csv_busy_times = Path("./data/cork/busy_times.csv")
    csv_flights = Path("./data/cork/flights_processed.csv")

    df_csv_busy_times = pd.read_csv(csv_busy_times)
    df_csv_flights = pd.read_csv(csv_flights)
    
    return df_csv_busy_times, df_csv_flights

def export_html(df_html_busy_times, df_html_flights):
    html_busy_times = Path("./data/cork/busy_times.html")
    html_flights = Path("./data/cork/flights_processed.html")

    df_html_busy_times.to_html(html_busy_times)
    df_html_flights.to_html(html_flights)
    
def convert_csv_to_html():
    df_csv_busy_times,  df_csv_flights = read_csv()
    export_html(df_csv_busy_times, df_csv_flights)
    
def move_file(source, destination):
    
    try:
        shutil.move(source, destination)
        print(f"Moved {source} to {destination}")
    except Exception as e:
        print(f"Error: {e}")
        
def main():
    convert_csv_to_html()
    
    source_file = './server/html'
    destination_dir = './'
    move_file(source_file, destination_dir)
    
if __name__ == "__main__":
    main()

    
    
    




