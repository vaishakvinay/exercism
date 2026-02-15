def line_up(name, number):

    num =str(number)

    if len(num) > 1 and num[-2] == "1":
        suffix = "th"

    elif num[-1] == "1" :
        suffix = "st"
    elif num[-1] == "2":
        suffix = "nd"
    elif num[-1] == "3":
        suffix = "rd"
    else:
        suffix = "th"

    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"
