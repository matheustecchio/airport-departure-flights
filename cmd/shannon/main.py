from shannon.process_data import process_data
from shannon.scrap import scrap
from shannon.convert_csv_to_html import convert_csv_to_html

def main():
    scrap()
    process_data()
    convert_csv_to_html()

if __name__ == "__main__":
    main()
