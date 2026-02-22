"""Convert a number from one base to another."""

def rebase(input_base, digits, output_base):
    """Rebase digits from input_base to output_base."""

    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    
    if not digits:
        return [0]

    for d in digits:
        if d < 0 or d >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

 
    decimal_value = 0
    for d in digits:
        decimal_value = decimal_value * input_base + d

    
    if decimal_value == 0:
        return [0]

   
    output_digits = []
    while decimal_value > 0:
        output_digits.append(decimal_value % output_base)
        decimal_value //= output_base

    output_digits.reverse()
    return output_digits
