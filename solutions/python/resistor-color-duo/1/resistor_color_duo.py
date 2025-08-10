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


def value(colors):

    # Take only first two colors
    first_two = colors[:2]
    result_str = ""

    for color in first_two:
        val = col.get(color)
        if val is None:
            raise ValueError(f"Invalid color: {color}")
        result_str += str(val)

    # Convert the concatenated string to int and return
    return int(result_str)
