def commands(binary_str):
    # Convert binary string → integer
    number = int(binary_str, 2)

    result = []

    # Check each bit using bitwise AND
    if number & 1:
        result.append("wink")

    if number & 2:
        result.append("double blink")

    if number & 4:
        result.append("close your eyes")

    if number & 8:
        result.append("jump")

    # Reverse flag (5th bit = 16)
    if number & 16:
        result.reverse()

    return result



    
