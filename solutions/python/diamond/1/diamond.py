def rows(letter):

    n = ord(letter) - ord('A')
    diamond = []

    
    for i in range(ord('A'), ord(letter) + 1):

        row_index = i - ord('A')
        ch = chr(i)

        outer_spaces = n - row_index
        if row_index == 0:
            line = " " * outer_spaces + ch +" " * outer_spaces 
        else:
            inner_spaces = 2 * row_index - 1
            line = " " * outer_spaces + ch + " " * inner_spaces + ch+" " * outer_spaces

        diamond.append(line)

    for i in range(ord(letter) - 1, ord('A') - 1, -1):

            row_index = i - ord('A')
            ch = chr(i)

            outer_spaces = n - row_index
            if row_index == 0:
                line = " " * outer_spaces + ch +" " * outer_spaces 
            else:
                inner_spaces = 2 * row_index - 1
                line = " " * outer_spaces + ch + " " * inner_spaces + ch+" " * outer_spaces

            diamond.append(line)

    return diamond