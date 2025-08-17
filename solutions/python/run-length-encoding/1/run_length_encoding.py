def decode(string):
    if not string:
        return ""

    result = ""
    count_str = ""

    for ch in string:
        if ch.isdigit():
            count_str += ch
        else:
            count = int(count_str) if count_str else 1
            result += ch * count
            count_str = ""   # reset

    return result


def encode(string):
    if not string:
        return ""

    result = ""
    current_run_character = string[0]
    run_length = 1

    for i in range(1, len(string)):
        current_char = string[i]
        if current_char == current_run_character:
            run_length += 1
        else:
            if run_length == 1:
                result += current_run_character
            else:
                result += str(run_length) + current_run_character
            current_run_character = current_char
            run_length = 1

    # flush last run
    if run_length == 1:
        result += current_run_character
    else:
        result += str(run_length) + current_run_character

    return result