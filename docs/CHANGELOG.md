# CHANGELOG

All notable changes to this project will be documented in this file.
To know about supported security versions, see [SECURITY](./SECURITY.md)

## Version 1.3 - 2026-08-13

### Added

- Responsive airport dashboard redesign with accessible navigation and improved empty-data states.
- Project icon and browser favicon.
- Local dashboard server that refreshes departure data before each top-level page load.
- No-cache HTML responses and an HTTP 503 error page for failed refreshes.
- Project-specific `AGENT.md` and `CLAUDE.md` development guidance.

### Changed

- Generated table documents now load their stylesheet before becoming visible.
- Installation requirements now contain only the application dependencies and a compatible Twisted version.
- Scraper execution now uses the active Python interpreter and the repository's Scrapy settings.
- Pipeline failures now raise reusable exceptions so both the command-line entry point and local server report the failed stage correctly.
- Setup and usage documentation now covers virtual environments, the local server, and one-shot refreshes.

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
