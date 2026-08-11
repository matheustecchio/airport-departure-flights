try:
    from process_data import process_data
    from scrap import scrap
    from convert_csv_to_html import convert_csv_to_html
except ModuleNotFoundError as error:
    raise SystemExit(
        f"Missing Python dependency: {error.name}\n"
        "Install the project dependencies with:\n"
        "  python3 -m pip install -r requirements.txt"
    ) from error

airport_list = ["cork", "dublin", "shannon"]

def main():
    for airport in airport_list:
        try:
            scrap(airport)
        except Exception as e:
            print(f"Error occurred while scraping {airport}: {str(e)}")
            exit(1)
        else:
            print(f"Data scraping completed successfully for {airport}.")
        
        try:
            process_data(airport)
        except Exception as e:
            print(f"Error occurred while processing {airport}: {str(e)}")
            exit(1)
        else:
            print(f"Data processing completed successfully for {airport}.")
        
        try:
            convert_csv_to_html(airport)
        except Exception as e:
            print(f"Error occurred while converting {airport} data to HTML: {str(e)}")
            exit(1)
        else:
            print(f"Data conversion to HTML completed successfully for {airport}.")

if __name__ == "__main__":
    main()
