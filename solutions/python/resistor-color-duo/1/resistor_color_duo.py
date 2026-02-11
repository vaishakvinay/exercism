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


def value(colors):
    
    result=[]


    first = RESISTOR_COLOR[colors[0]]
    second = RESISTOR_COLOR[colors[1]]

    return first * 10 + second