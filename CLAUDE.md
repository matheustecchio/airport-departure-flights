# Repository Instructions

## Project overview

- This application scrapes current departure information for Cork, Dublin, and Shannon airports, estimates minimum passenger volume by hourly window, and renders static dashboard pages.
- Use Python 3.9 through 3.12. Direct dependencies are pinned in `requirements.txt`; the browser-facing code is plain HTML, CSS, and JavaScript.
- Run Python entry points from the repository root. Their data paths are repository-relative.

## Repository map

- `cmd/main.py` orchestrates scrape, processing, and HTML conversion for every supported airport.
- `cmd/scrap.py` invokes Scrapy and writes `data/<airport>/raw_flights.csv`.
- `cmd/process_data.py` adds aircraft capacity estimates and writes `busy_times.csv` and `flights_processed.csv`.
- `cmd/convert_csv_to_html.py` converts the processed CSV files into the HTML tables embedded by the dashboard.
- `scrap_airport_flights/spiders/` contains one FlightAware spider per airport. `scrap_airport_flights/settings.py` contains the Scrapy settings.
- `web/index.html` is the landing page; `web/{cork,dublin,shannon}.html`, `web/style.css`, and `web/script.js` implement the airport dashboards.
- `data/` is generated runtime output and is ignored by Git. Do not hand-edit or commit it.
- `docs/docs.md` documents scraped selectors and the output schema. Contributor, security, release-history, and community policies live under `docs/`.

## Setup and operation

- Create and activate an isolated environment on Linux or macOS:

  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  python3 -m pip install --upgrade pip
  python3 -m pip install -r requirements.txt
  ```

- On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1` and use `python` in place of `python3`.
- Refresh all airport data from the repository root with:

  ```bash
  python3 cmd/main.py
  ```

  This command requires network access, contacts FlightAware, replaces generated airport files under `data/`, and exits after the first airport failure.
- After generating data, open `web/index.html` in a browser. Airport pages load their generated tables from `../data/<airport>/`.

## Architecture and implementation constraints

- Preserve the pipeline order: scrape raw CSV, process CSV, then convert the results to HTML. Keep the column contract documented in `docs/docs.md` consistent across spiders and processors.
- Keep airport support synchronized across `cmd/main.py`, `scrap_airport_flights/spiders/<airport>.py`, and `web/<airport>.html`; update landing-page and navigation links when the supported set changes.
- Treat FlightAware markup and its CSS selectors as an external interface. If a selector changes, update every affected spider and `docs/docs.md`, then verify that all yielded lists remain aligned before indexing them by flight number.
- Keep aircraft capacity mapping changes in `cmd/process_data.py` explicit. Unknown aircraft currently produce a missing `Minimum Passengers` value; do not silently invent a capacity.
- Preserve `ROBOTSTXT_OBEY = True` and the existing conservative Scrapy behavior unless a deliberate, documented change requires otherwise.
- The airport pages embed same-origin pandas-generated tables in iframes. Keep iframe source paths, empty-state behavior, height validation, and accessibility labels working together when changing `web/`.
- Use `pathlib.Path` for filesystem paths in Python and preserve cross-platform command behavior through `sys.executable` where subprocesses are involved.

## Verification

- There is currently no configured automated test, lint, type-check, build, or CI suite. Do not claim those checks ran.
- For scraper or end-to-end pipeline changes, run `python3 cmd/main.py` only when network access and replacement of ignored `data/` output are appropriate. Confirm all three airport directories contain non-empty raw CSV, processed CSV, busy-times CSV, and both generated HTML tables.
- For processing changes, inspect representative boundary times, empty hourly buckets, past-versus-future filtering, unknown aircraft models, and generated CSV columns.
- For `web/` changes, generate data first, then manually check `web/index.html` plus all three airport pages at desktop and narrow widths. Verify navigation, keyboard focus, iframe table styling and sizing, and the missing-data state.
- For documentation-only changes, review links, commands, and path names; running the data pipeline is unnecessary.
- Before handoff, inspect `git diff` and run `git diff --check`. Keep unrelated user changes untouched.

## Documentation synchronization

- Update `README.md` when setup steps, supported Python versions, dependencies, runtime commands, supported airports, or user-visible behavior change.
- Update `docs/docs.md` when scraper selectors, scraped fields, or output columns change.
- Add user-visible release notes to `docs/CHANGELOG.md` when preparing a release-worthy change.
- Keep `AGENT.md` and `CLAUDE.md` substantively synchronized whenever repository guidance changes.

## Git and pull requests

- Inspect status and the current branch before editing. The repository may contain uncommitted user work; never discard, overwrite, or include unrelated changes.
- Follow `docs/CONTRIBUTING.md`: use a focused `feature/<name>` branch for code or `docs/<name>` for documentation, make a concise prefixed commit, push the branch, and open a pull request using `docs/PULL_REQUEST__TEMPLATE`.
- Do not commit directly to `main`. Stage files deliberately and keep each commit to one logical change.
- Do not commit, amend, force-push, rewrite history, merge, push, or open a pull request unless the user explicitly requests the relevant action.

## Security and change safety

- Never add credentials, tokens, private keys, production data, sensitive URLs, or secret-bearing logs. Use placeholders in examples and follow `docs/SECURITY.md` for vulnerability reports.
- Do not weaken input validation, robots.txt compliance, iframe message validation, or other safety controls merely to make a change work.
- Avoid editing dependencies, caches, virtual environments, generated data, or build artifacts unless the task specifically targets them.
- Do not install dependencies, contact external services, publish, release, or deploy without explicit user intent. Review diffs for secrets, debug output, unrelated files, and generated noise before handoff.
