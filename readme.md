# Chemical Engineering Toolbox

> **An open-source study and calculation companion for Chemical Engineering students.**

## Features

### Engineering Calculators
- Reynolds Number Calculator
- Pump Head Calculator
- Pipe Velocity Calculator

### Educational Features
- Formula Used
- Engineering Interpretation
- Engineering Tips
- Typical Operating Ranges
- Industrial Applications
- Common Mistakes

### Core Features
- Universal Unit Conversion
- Robust Input Validation
- Professional Formatted Output
- Persistent Calculation History
- CSV History Storage
- Modular Architecture
- Reusable Utility Modules

### Utility Modules
- Validation Utilities
- Unit Conversion Utilities
- Geometry Utilities
- Input Helper Utilities
- Formatter Utilities

## Project Structure

```text
Chemical Engineering Toolbox/
│
├── calculators/
│   ├── pipe_velocity.py
│   ├── pump_head.py
│   └── reynolds.py
│
├── resources/
│   ├── dimensionless_numbers/
│   │   └── reynolds.py
│   └── fluid_mechanics/
│       ├── pipe_velocity.py
│       └── pump_head.py
│
├── utils/
│   ├── formatter.py
│   ├── geometry.py
│   ├── input_helper.py
│   ├── units.py
│   └── validation.py
│
├── config.py
├── history.py
├── history.csv
├── main.py
├── README.md
└── CHANGELOG.md
```

## Current Calculators

### Reynolds Number Calculator
Calculates the Reynolds number of a fluid flowing through a pipe and classifies the flow regime as:
- Laminar
- Transitional
- Turbulent

### Pump Head Calculator
Calculates the required pump head from pressure drop and fluid density.

### Pipe Velocity Calculator
Calculates the average fluid velocity using volumetric flow rate and pipe diameter.

## Highlights

- Built using Python
- Modular architecture for easy expansion
- Reusable utility modules
- Automatic calculation history
- CSV history persistence
- User-friendly console interface
- Robust input validation

## Requirements

- Python 3.10 or later

## How to Run

Clone the repository:

```bash
git clone https://github.com/smitpsolanki/chemical-engineering-toolbox.git
```

Go to the project folder:

```bash
cd chemical-engineering-toolbox
```

Run the application:

```bash
python main.py
```

## Current Version

**v0.9.1**

## Project Vision

Chemical Engineering Toolbox is an open-source study and calculation companion
designed specifically for Chemical Engineering students.

The objective is not only to perform engineering calculations but also to help
students understand the concepts behind them through engineering explanations,
practical tips, typical operating ranges, industrial applications, and common
mistakes.

The project is being developed incrementally with a modular architecture,
making it easy to maintain, extend, and learn from.

## Author

**Smit Solanki**