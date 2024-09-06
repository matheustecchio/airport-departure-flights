from cork.process_data import process_data
from cork.scrap import scrap
from cork.convert_csv_to_html import convert_csv_to_html

def main():
    print("\nCork is running...")
    scrap()
    process_data()
    convert_csv_to_html()

if __name__ == "__main__":
    main()

