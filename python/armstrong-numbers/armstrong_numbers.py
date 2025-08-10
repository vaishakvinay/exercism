def is_armstrong_number(number):
    num_str = str(number)          # Convert to string to get individual digits
    num_digits = len(num_str)      # Number of digits
    total = 0

    for digit in num_str:
        total += int(digit) ** num_digits
    return total == number 