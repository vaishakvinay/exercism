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

def label(colors):
    

    


    first = RESISTOR_COLOR[colors[0]]
    second = RESISTOR_COLOR[colors[1]]
    third=RESISTOR_COLOR[colors[2]]
    

    
    value = int(str(first) + str(second)) * (10 ** third)

    
    if value >= 1_000_000_000:
        return f"{value // 1_000_000_000} gigaohms"

    elif value >= 1_000_000:
        return f"{value // 1_000_000} megaohms"

    elif value >= 1_000:
        return f"{value // 1_000} kiloohms"

    else:
        return f"{value} ohms"