# Changelog

All notable changes to this project will be documented in this file.

---
## [v0.9.1] - 2026-07-03

###  Added

#### Presentation Framework
- Added `formatter.py`
- Added reusable `print_header()`
- Added reusable `print_section()`
- Added reusable `print_result()`
- Added reusable `print_paragraph()`
- Added reusable `print_dictionary()`
- Added reusable `print_footer()`

#### Educational Resources
- Added educational resources for Reynolds Number
- Added educational resources for Pump Head
- Added educational resources for Pipe Velocity

#### Educational Content
- Formula Used
- Engineering Interpretation
- Engineering Tips
- Typical Operating Ranges
- Industrial Applications
- Common Mistakes

### Improved

- Reynolds Number Calculator redesigned with educational output.
- Pump Head Calculator redesigned with educational output.
- Pipe Velocity Calculator redesigned with educational output.
- Improved readability with professional report formatting.
- Enhanced console user experience.

### Refactored

- Separated engineering calculations from educational content.
- Introduced presentation layer for output formatting.
- Improved modular project architecture.
- Increased code reusability through formatter utilities.

---

## [v0.9] - 2026-07-03

### Added
- Added universal unit conversion framework.
- Added `units.py` utility module.
- Added reusable `convert_flow_rate()` function.
- Added reusable `convert_length()` function.
- Added reusable `convert_pressure()` function.
- Added reusable `select_option()` helper for menu selections.
- Added reusable `get_positive_integer()` validation function.

### Improved
- Updated Reynolds Number Calculator to support multiple input units.
- Updated Pump Head Calculator to support multiple input units.
- Updated Pipe Velocity Calculator to support multiple input units.
- Improved code reusability through shared unit conversion utilities.
- Enhanced modular architecture.

### Fixed
- Minor improvements to input validation and menu handling.

---

## v0.8 - Pipe Velocity Calculator

### Added
- Added Pipe Velocity Calculator.
- Added `geometry.py` utility module.
- Added reusable `calculate_pipe_area()` function.
- Added `get_positive_float()` validation function.
- Improved input validation across calculators.

### Fixed
- Fixed history persistence after clearing history.
- History file is now correctly overwritten when history is empty.

---

## v0.7 - Persistent History Update

### Added

- Automatic loading of history from `history.csv` at startup.
- Automatic saving of history when exiting the application.
- CSV export support for calculation history.
- Date and time logging for every calculation.

### Improved

- Cleaner project architecture.
- Better user experience through automatic history persistence.
- History entries now include calculator name, date, time, and result.

### Fixed

- Correct timestamp is now recorded for each calculation.
- Improved history management and file handling.

---

## v0.6 - History Enhancement

### Added

- Date and time support for history.
- Better history display formatting.

---

## v0.5 - History Management

### Added

- Show calculation history.
- Clear history functionality.

---

## v0.4 - Project Organization

### Added

- Modular project structure.
- Configuration file (`config.py`).
- Separate history module.

---

## v0.3 - Pump Head Calculator

### Added

- Pump Head Calculator.

---

## v0.2 - Reynolds Number Calculator

### Added

- Reynolds Number Calculator.

---

## v0.1 - Initial Release

### Added

- Initial project structure.
- Main application menu.