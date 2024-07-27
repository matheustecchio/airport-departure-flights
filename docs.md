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

## Cmd
At the root of the application, runs:

```bash
python main.py
```