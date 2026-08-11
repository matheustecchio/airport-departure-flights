import os
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
SPIDERS_DIR = PROJECT_ROOT / "scrap_airport_flights" / "spiders"
DATA_DIR = PROJECT_ROOT / "data"


def scrap(airport: str):
    spider_path = SPIDERS_DIR / f"{airport}.py"
    output_path = DATA_DIR / airport / "raw_flights.csv"

    if not spider_path.is_file():
        raise ValueError(f"Unknown airport spider: {airport}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.unlink(missing_ok=True)

    subprocess.run(
        [
            sys.executable,
            "-m",
            "scrapy",
            "runspider",
            str(spider_path),
            "-O",
            str(output_path),
        ],
        cwd=PROJECT_ROOT,
        check=True,
        env={
            **os.environ,
            "SCRAPY_SETTINGS_MODULE": "scrap_airport_flights.settings",
        },
    )

    if not output_path.is_file() or output_path.stat().st_size == 0:
        raise RuntimeError(
            f"Scraper produced no flight data for {airport}. "
            "FlightAware may be unavailable or its page structure may have changed."
        )


if __name__ == "__main__":
    scrap("cork")
