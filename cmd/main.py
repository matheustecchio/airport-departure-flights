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


def run_stage(airport, stage_name, action):
    try:
        action(airport)
    except Exception as error:
        raise RuntimeError(
            f"Error occurred while {stage_name} {airport}: {error}"
        ) from error

    print(f"Data {stage_name} completed successfully for {airport}.")


def main():
    for airport in airport_list:
        run_stage(airport, "scraping", scrap)
        run_stage(airport, "processing", process_data)
        run_stage(airport, "conversion to HTML", convert_csv_to_html)

if __name__ == "__main__":
    try:
        main()
    except RuntimeError as error:
        raise SystemExit(str(error)) from error
