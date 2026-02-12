def encode(message, rails):

    if rails == 1:
        return message

    rails_list = [""] * rails

    rail = 0
    direction = 1

    for char in message:
        rails_list[rail] += char

        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    return "".join(rails_list)

def decode(encoded_message, rails):

    if rails == 1:
        return encoded_message

    
    pattern = []
    rail = 0
    direction = 1

    for _ in encoded_message:
        pattern.append(rail)

        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    
    rail_counts = [pattern.count(r) for r in range(rails)]

  
    rails_list = []
    index = 0

    for count in rail_counts:
        rails_list.append(encoded_message[index:index + count])
        index += count

    rail_positions = [0] * rails
    result = ""

    for rail in pattern:
        result += rails_list[rail][rail_positions[rail]]
        rail_positions[rail] += 1

    return result

