def encode(plain_text):
    result = ''
    for ch in plain_text:
        if 'A' <= ch <= 'Z':
            # Convert uppercase to lowercase
            ch = chr(ord(ch) + 32)

        if 'a' <= ch <= 'z':
            # Apply Atbash cipher for lowercase letters
            encoded_ch = chr(ord('z') - (ord(ch) - ord('a')))
            result += encoded_ch
        elif '0' <= ch <= '9':
            # Keep digits unchanged
            result += ch
        else:
            # Ignore other characters (punctuation, spaces, etc.)
            continue

    # Group result into chunks of 5 characters
    grouped = ''
    count = 0
    for ch in result:
        if count == 5:
            grouped += ' '
            count = 0
        grouped += ch
        count += 1

    return grouped


def decode(ciphered_text):
    result = ''
    for ch in ciphered_text:
        if ch == ' ':
            continue
        if 'a' <= ch <= 'z':
            # Atbash decode for lowercase letters
            decoded_ch = chr(ord('z') - (ord(ch) - ord('a')))
            result += decoded_ch
        elif '0' <= ch <= '9':
            result += ch
        else:
            # Ignore any other characters
            continue

    return result

