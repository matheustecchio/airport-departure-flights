# Airport Departure Flights

Application to return all departure flights information for a specific airport in Ireland.

This project began to check how busy the airport gate's area would be. This information is very important for staff working in the gate area, as I was when I created this application.

### Why not to create the arrival flights?
Having an arriving flights section wouldn't be useful for the purpose of the project, which is to check how busy it will be, because most of the customers in the landing area of the airport are the airport's staffs and non-passengers in general, making it difficult to predict with flight information.

# Technologies
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

## Requirements

- Python 3.9 through Python 3.12
- `pip`
- An internet connection for installing packages and retrieving flight data

The direct Python dependencies are listed in [requirements.txt](./requirements.txt).

## Installation

Clone the repository and move into it:

```bash
git clone https://github.com/matheustecchio/airport-departure-flights.git
cd airport-departure-flights
```

Create an isolated environment and install the dependencies on Linux or macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

On Windows PowerShell, use:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## How to use

Activate the virtual environment whenever you open a new terminal, then run the dashboard server from the repository root:

```bash
source .venv/bin/activate
python3 cmd/server.py
```

On Windows, use `python cmd/server.py` after activating the environment.

Open [http://127.0.0.1:8000/web/index.html](http://127.0.0.1:8000/web/index.html) while the server is running. Every landing or airport dashboard page load retrieves current departure data, processes it, and regenerates the tables under `data/` before returning the page. Stop the server with `Ctrl+C`.

The refresh runs before the page is returned, so a reload can take several seconds depending on the upstream response. Opening `web/index.html` directly with a `file://` URL only displays existing generated data and cannot run Python.

To refresh the generated data once without starting the server, run:

```bash
python3 cmd/main.py
```

If you see `ModuleNotFoundError`, verify that the virtual environment is active and run:

```bash
python3 -m pip install -r requirements.txt
```

If a live refresh fails, the server returns a `503` page with the failed pipeline stage. Check the server terminal for the Scrapy details and reload to try again.

---

## 📅 Releases and Updates
All notable changes to this project will be documented at [CHANGELOG.md](./docs/CHANGELOG.md).


## 📜 Code of Conduct

We expect all contributors to follow our [Code of Conduct](./docs/CODE_OF_CONDUCT.md). Please read it to understand the standards of behavior we expect.


## 🔁 Contributing

We welcome contributions! To contribute to this project, please check our [CONTRIBUTING.md](./docs/CONTRIBUTING.md). This document provides guidelines on how to submit issues and pull requests.

## 🫂 Acknowledgment

This project was possible thanks to the efforts of many talented people. We appreciate everyone who played a part in its creation.

For a detailed list of contributors, please see [ACKNOWLEDGMENTS.md](./docs/ACKNOWLEDGMENTS.md).

## 🛡️ Security

We take security seriously. For details on how to report vulnerabilities and our security practices, please refer to our [SECURITY.md](./docs/SECURITY.md).

We will announce security updates via Security Advisories on our Security page and document them in the [CHANGELOG.md](./docs/CHANGELOG.md). Stay informed by monitoring these channels regularly.
  
## 📝 License

This project is licensed under the [MIT License](./docs/LICENSE).

By using this project, you agree to follow and obey the terms and conditions of the license.

---

***Copyright (c) 2024 [Matheus Tecchio](https://github.com/matheustecchio).***
