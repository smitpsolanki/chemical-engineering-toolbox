LAMINAR_LIMIT = 2300
TRANSITION_LIMIT = 4000

FORMULA = "Re = (Density * Velocity * Diameter) / Dynamic Viscosity"

FLOW_REGIMES = {
    "Laminar": {
    "interpretation": (
        "The flow is laminar, indicating that viscous forces dominate "
        "over inertial forces. The fluid moves in smooth, orderly layers "
        "with minimal mixing."
    ),
    "tip": (
        "Laminar flow produces low pressure losses but offers poorer "
        "mixing and heat transfer. It is commonly encountered in "
        "microfluidic systems, lubrication, and very slow flows."
    )
},
    "Transition": {
    "interpretation": (
        "The flow is in the transition region, where it may alternate "
        "between laminar and turbulent behavior. Small disturbances can "
        "significantly affect the flow pattern."
    ),
    "tip": (
        "Flow in this region is generally avoided in engineering design "
        "because it is unstable and difficult to predict accurately."
    )
},
    "Turbulent": {
    "interpretation": (
        "The flow is turbulent, indicating that inertial forces dominate "
        "over viscous forces. The fluid experiences vigorous mixing and "
        "random velocity fluctuations."
    ),
    "tip": (
        "Turbulent flow enhances mixing and heat transfer but increases "
        "pressure losses and pumping power requirements. Most industrial "
        "piping systems operate in the turbulent regime."
    )
}
}