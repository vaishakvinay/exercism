num = ('no','one', 'two', 'three', 'four', 'five', 'six',
        'seven', 'eight', 'nine' , 'ten')
bottles = ('bottles', 'bottle')
def recite(start, take=1):
    result = []
    for i in range(start, start - take, -1):
        one_two = (f"{num[i]} green {bottles[i == 1]} hanging on the wall,").capitalize()
        result.extend([one_two] * 2) 
        result.append('And if one green bottle should accidentally fall,')
        result.append(f"There'll be {num[i - 1]} green {bottles[i == 2]} hanging on the wall.")

        if take > 1 and i > start - take + 1:
            result.append('')

    return result