# CHANGELOG

All notable changes to this project will be documented in this file.
To know about supported security versions, see [SECURITY](./SECURITY.md)

## Unreleased

### Added

- Local dashboard server that refreshes departure data before each top-level page load.
- No-cache HTML responses and an HTTP 503 error page for failed refreshes.

### Changed

- Pipeline failures now raise reusable exceptions so both the command-line entry point and local server report the failed stage correctly.

## Version 1.2 - 2024-09-13

### Added
- Index page
- Better styling
- Responsive interface

### Removed
- Repeated code in cmd/ 

## Version 1.1 - 2024-09-07

### Added
- Supports Dublin and Shannon Airports.
- More readable web page.

### Removed
- Jupyter Notebook file for processing data.

## Version 1.0 - 2024-09-06

### Added
- Application to view live departure flights from Cork Airport.
