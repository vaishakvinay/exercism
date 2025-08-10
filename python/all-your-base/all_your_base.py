def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2") 
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    for d in digits:
        if d < 0 or d >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        
    decimal = 0
    for index, d in enumerate(digits[::-1]):
        decimal += d * input_base ** index

    if decimal == 0:
        return [0]

    output_digits = []
    while decimal > 0:
        output_digits.append(decimal % output_base)
        decimal //= output_base

    return output_digits[::-1]