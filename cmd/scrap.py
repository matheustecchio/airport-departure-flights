import subprocess
import platform

def scrap(airport: str):
    windows_script = "scrapy runspider .\\scrap_airport_flights\\spiders\\" + airport + ".py -O .\\data\\cork\\raw_flights.csv"
    unix_script = "scrapy runspider scrap_airport_flights/spiders/" + airport + ".py -O ./data/" + airport + "/raw_flights.csv"

    try:
        if platform.system() == "Windows":
            process = subprocess.run(["powershell", "-Command", windows_script], capture_output=True, text=True)
        else:
            process = subprocess.run(unix_script, shell=True, capture_output=True, text=True)
    except:
        print("An error occurred while executing the scraping script.")
        exit(1)  
        
if __name__ == "__main__":
    scrap()
