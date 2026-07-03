# Chemical Engineering Toolbox

A modular Python-based toolbox developed for common Chemical Engineering calculations.

## Features

- Reynolds Number Calculator
- Pump Head Calculator
- Pipe Velocity Calculator
- Calculation History
- Automatic History Save & Load
- CSV History Export
- Robust Input Validation
- Modular Project Structure
- Reusable Geometry Utilities

Chemical Engineering Toolbox/
│
├── calculators/
│   ├── pump_head.py
│   ├── reynolds.py
│   └── pipe_velocity.py
│
├── utils/
│   ├── geometry.py
│   ├── input_helper.py
│   └── validation.py
│
├── config.py
├── history.py
├── history.csv
├── main.py
├── README.md
└── CHANGELOG.md

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

**v0.8**

## Future Plans

- Universal Unit Conversion System
- Pressure Drop Calculator
- Pump Power Calculator
- Heat Exchanger Utilities
- Pipe Flow Utilities
- Additional Chemical Engineering Calculators

## Author

**Smit Solanki**