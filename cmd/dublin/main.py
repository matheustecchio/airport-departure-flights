from dublin.process_data import process_data
from dublin.scrap import scrap
from dublin.convert_csv_to_html import convert_csv_to_html

def main():
    print("\nDublin is running...")
    scrap()
    process_data()
    convert_csv_to_html()

if __name__ == "__main__":
    main()
