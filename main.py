import subprocess
import platform

script = """
scrapy runspider scrap_airport_flights/spiders/flights.py -O flights.json
"""

if platform.system() == "Windows":
    process = subprocess.run(["powershell", "-Command", script], capture_output=True, text=True)
else:
    process = subprocess.run(script, shell=True, capture_output=True, text=True)
    
print(process.stdout)
print(process.stderr)
print("Data scrapping completed successfully!")
