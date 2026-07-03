# Changelog

All notable changes to this project will be documented in this file.

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