def is_pangram(sentence):

    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    letters_in_sentence = set(sentence.lower())
    return alphabet.issubset(letters_in_sentence)

