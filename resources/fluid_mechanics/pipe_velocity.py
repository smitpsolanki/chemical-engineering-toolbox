FORMULA = "Velocity = Volumetric Flow Rate / Cross-sectional Area"

INTERPRETATION = (
    "Pipe velocity represents the average speed of fluid flowing through "
    "a pipe. It is determined by the volumetric flow rate and the pipe's "
    "cross-sectional area."
)

ENGINEERING_TIP = (
    "Selecting an appropriate flow velocity is important. Very low "
    "velocities may cause sedimentation and poor mixing, while very high "
    "velocities increase pressure losses, noise, and pipe erosion."
)

TYPICAL_RANGES = {
    "Water Distribution Systems": "0.6 - 3.0 m/s",
    "Process Liquids": "1.0 - 3.0 m/s",
    "Steam Lines": "20 - 40 m/s",
    "Compressed Air": "6 - 10 m/s"
}

INDUSTRIAL_APPLICATIONS = (
    "Pipe velocity calculations are used in pipeline design, pump sizing, "
    "heat exchanger design, process equipment sizing, and fluid transport "
    "systems."
)

COMMON_MISTAKES = (
    "Always convert the flow rate to m³/s and the pipe diameter to metres "
    "before calculation. An incorrect unit conversion will produce an "
    "incorrect velocity."
)