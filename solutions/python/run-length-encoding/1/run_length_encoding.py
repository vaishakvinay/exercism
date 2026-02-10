def decode(string):

    num = ""
    new = ""

    for ch in string:

        if ch.isdigit():
            num += ch

        else:
            count = int(num) if num else 1
            new += ch * count
            num = ""          

    return new


def encode(string):

    if string == "":
        return ""

    new = ""
    count = 1

    for i in range(1, len(string)):

        if string[i] == string[i - 1]:
            count += 1
        else:
            if count == 1:
                new += string[i - 1]
            else:
                new += str(count) + string[i - 1]

            count = 1

    # last group
    if count == 1:
        new += string[-1]
    else:
        new += str(count) + string[-1]

    return new
