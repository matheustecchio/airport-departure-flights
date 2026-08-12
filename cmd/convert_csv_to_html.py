import pandas as pd
from pathlib import Path


STYLESHEET_PATH = "../../web/style.css"


def read_csv(airport:str):
    csv_busy_times = Path("./data/"+ airport + "/busy_times.csv")
    csv_flights = Path("./data/" + airport + "/flights_processed.csv")

    df_csv_busy_times = pd.read_csv(csv_busy_times)
    df_csv_flights = pd.read_csv(csv_flights)
    
    return df_csv_busy_times, df_csv_flights


def dataframe_page(dataframe, title: str) -> str:
    table = dataframe.to_html(border=0)

    return f"""<!DOCTYPE html>
<html lang="en" class="embedded-data">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link id="airport-dashboard-styles" rel="stylesheet" href="{STYLESHEET_PATH}">
</head>
<body>
{table}
</body>
</html>
"""


def export_html(df_html_busy_times, df_html_flights, airport:str):
    html_busy_times = Path("./data/" + airport + "/busy_times.html")
    html_flights = Path("./data/" + airport + "/flights_processed.html")

    html_busy_times.write_text(
        dataframe_page(df_html_busy_times, f"{airport.title()} busy times"),
        encoding="utf-8",
    )
    html_flights.write_text(
        dataframe_page(df_html_flights, f"{airport.title()} departures"),
        encoding="utf-8",
    )
    
def convert_csv_to_html(airport:str):
    df_csv_busy_times,  df_csv_flights = read_csv(airport)
    
    export_html(df_csv_busy_times, df_csv_flights, airport)
    
if __name__ == "__main__":
    default_airport = "cork"
    convert_csv_to_html(default_airport)
