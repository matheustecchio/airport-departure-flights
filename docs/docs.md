## Scrapped HTML elements

| HTML path | Description | Example |
|---|---|---|
| #scheduled-board td:nth-child(4) i | return the depart time | '17:45 IST'
| #scheduled-board .flight-ident+ td a | return the shorted version of the aircraft model | 'B738'
| #scheduled-board .hint+ span a | return the destination airport IATA code | 'LTN'
| #scheduled-board .hint span | return the destination airport name | 'London Luton'
| #scheduled-board .flight-ident a | return the flight number | 'EI894','FR7721'

## Json File output

**Date**: Date which the program ran.

**Time**: Time which the program ran.

**Airport Name**: Airport where the flights are leaving from.

**Departure Time**: Schedule flight departure time.

**Aircraft Model**: Aircraft model which the flight was scheduled.

**Destination IATA**: IATA code of the destination airport.

**Destination Name**: Airport name of the destination airport.

**Flight Number**: Number of the flight.

> Some `Destination Name` has Unicode characters which represent non-ASCII characters.

## Dashboard refresh server

Run `python3 cmd/server.py` from the repository root and open `http://127.0.0.1:8000/web/index.html`.

For each request to a top-level page (`index.html`, `cork.html`, `dublin.html`, or `shannon.html`), the server:

1. Runs the full pipeline in `cmd/main.py` for Cork, Dublin, and Shannon.
2. Replaces the ignored files under `data/<airport>/`.
3. Returns the requested page only after all generated tables are ready.

Requests for CSS, JavaScript, images, and generated iframe HTML do not start another refresh. Refreshes are serialized to prevent concurrent writes to `data/`, and HTML responses use no-cache headers so the browser requests the latest generated tables.

If any scraping, processing, or conversion stage fails, the server returns HTTP `503` rather than serving a page with partially refreshed data. The server binds to `127.0.0.1` by default; do not expose it publicly without adding appropriate access controls and request throttling.

Opening `web/index.html` directly does not run Python. Use `python3 cmd/main.py` for a one-time refresh when the HTTP server is not needed.
