col={
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

def label(colors):
    first_two = colors[:2]
    multiplier_color = colors[2]
    result_str = ""

    for color in first_two:
        val = col.get(color)
        if val is None:
            raise ValueError(f"Invalid color: {color}")
        result_str += str(val)

    val3 = col.get(multiplier_color)
    if val3 is None:
        raise ValueError(f"Invalid color: {multiplier_color}")

    # Get raw number as int
    value = int(result_str) * (10 ** val3)

    # Determine suffix and scaled value
    if value >= 1_000_000_000:
        scaled = value // 1_000_000_000
        suffix = " gigaohms"
    elif value >= 1_000_000:
        scaled = value // 1_000_000
        suffix = " megaohms"
    elif value >= 1_000:
        scaled = value // 1_000
        suffix = " kiloohms"
    else:
        scaled = value
        suffix = " ohms"

    return f"{scaled}{suffix}"


