def encode(numbers):

    result = []

    for n in numbers:

   
        if n < 0:
            raise ValueError("negative numbers not supported")

       
        chunks = []

        while True:
            chunks.insert(0, n & 0x7F)
            n >>= 7
            if n == 0:
                break

       
        for i in range(len(chunks) - 1):
            chunks[i] |= 0x80

        
        result.extend(chunks)

    return result




def decode(bytes_):


    result = []
    value = 0
    building = False   # track if we are inside a number

    for b in bytes_:

        building = True

        data = b & 0x7F
        value = (value << 7) | data

        # Last byte of number
        if (b & 0x80) == 0:
            result.append(value)
            value = 0
            building = False

    # 🔴 Incomplete sequence check
    if building:
        raise ValueError("incomplete sequence")

    return result


