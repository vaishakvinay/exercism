def convert(input_grid):

    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    for row in input_grid:
        if len(row) % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")

    DIGITS = {
        " _ | ||_|   ": "0",
        "     |  |   ": "1",
        " _  _||_    ": "2",
        " _  _| _|   ": "3",
        "   |_|  |   ": "4",
        " _ |_  _|   ": "5",
        " _ |_ |_|   ": "6",
        " _   |  |   ": "7",
        " _ |_||_|   ": "8",
        " _ |_| _|   ": "9",
    }

    result = []

    for i in range(0, len(input_grid), 4):

        block = input_grid[i:i+4]
        line_digits = []
        width = len(block[0])

        for c in range(0, width, 3):

            digit_pattern = ""

            for r in block:
                digit_pattern += r[c:c+3]

            digit = DIGITS.get(digit_pattern, "?")
            line_digits.append(digit)

        result.append("".join(line_digits))

    return ",".join(result)
