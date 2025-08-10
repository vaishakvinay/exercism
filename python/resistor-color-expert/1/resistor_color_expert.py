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

t_b={
"grey" : 0.05,
"violet" : 0.1,
"blue" : 0.25,
"green" : 0.5,
"brown" : 1,
"red" : 2,
"gold" : 5,
"silver" : 10}

def resistor_label(colors):
    n = len(colors)

    if n == 1:
        if colors[0] != 'black':
            raise ValueError("Invalid 1-band resistor color")
        return "0 ohms"

    if n == 4:
        v1 = col.get(colors[0])
        v2 = col.get(colors[1])
        multiplier = col.get(colors[2])
        tolerance = t_b.get(colors[3])
        if None in (v1, v2, multiplier) or tolerance is None:
            raise ValueError("Invalid color band(s)")

        resistance = (v1 * 10 + v2) * (10 ** multiplier)


    elif n==5:
        v1 = col.get(colors[0])
        v2 = col.get(colors[1])
        v3 = col.get(colors[2])
        multiplier = col.get(colors[3])
        tolerance = t_b.get(colors[4])
        if None in (v1, v2, v3,multiplier) or tolerance is None:
            raise ValueError("Invalid color band(s)")

        resistance = (v1 * 100 + v2 * 10 + v3) * (10 ** multiplier)
        
        
    else:
        raise ValueError("Invalid number of color bands")
    
    if resistance >= 1_000_000:
        value = resistance / 1_000_000
        suffix = " megaohms"
    elif resistance >= 1_000:
        value = resistance / 1_000
        suffix = " kiloohms"
    else:
        value = resistance
        suffix = " ohms"

    # Remove decimal if integer
    if isinstance(value, float) and value.is_integer():
        value = int(value)

    return f"{value}{suffix} ±{tolerance}%"
    