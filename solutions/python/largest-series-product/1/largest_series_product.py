def largest_product(series, size):

    
    if len(series)<size:
        raise ValueError("span must not exceed string length")

    if size<1:
        raise ValueError("span must not be negative")

    if not series.isdigit():
        raise ValueError("digits input must only contain digits")

    if size == 0:
        return 1

    products = []

    for i in range(len(series) - size + 1):

        piece = series[i:i+size]   # slice

        product = 1

        for digit in piece:
            product *= int(digit)

        products.append(product)

    return max(products)