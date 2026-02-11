RESISTOR_COLOR = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

TOLERANCE = {
    "grey": "±0.05%",
    "violet": "±0.1%",
    "blue": "±0.25%",
    "green": "±0.5%",
    "brown": "±1%",
    "red": "±2%",
    "gold": "±5%",
    "silver": "±10%"
}


def resistor_label(colors):

    # ---------- 1 BAND ----------
    if len(colors) == 1:
        value = RESISTOR_COLOR[colors[0]]
        return f"{value} ohms"

    # ---------- 4 BAND ----------
    if len(colors) == 4:
        digits = (
            RESISTOR_COLOR[colors[0]] * 10
            + RESISTOR_COLOR[colors[1]]
        )
        multiplier = RESISTOR_COLOR[colors[2]]
        tolerance = TOLERANCE[colors[3]]

    # ---------- 5 BAND ----------
    else:
        digits = int(
            f"{RESISTOR_COLOR[colors[0]]}"
            f"{RESISTOR_COLOR[colors[1]]}"
            f"{RESISTOR_COLOR[colors[2]]}"
        )
        multiplier = RESISTOR_COLOR[colors[3]]
        tolerance = TOLERANCE[colors[4]]

    value = digits * (10 ** multiplier)

    # ---------- SCALE ----------
    if value >= 1_000_000_000:
        label = f"{value / 1_000_000_000:g} gigaohms"
    elif value >= 1_000_000:
        label = f"{value / 1_000_000:g} megaohms"
    elif value >= 1_000:
        label = f"{value / 1_000:g} kiloohms"
    else:
        label = f"{value:g} ohms"

    return f"{label} {tolerance}"
