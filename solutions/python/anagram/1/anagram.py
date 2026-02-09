def find_anagrams(word, candidates):

    word_clean = word.lower()
    sorted_word = sorted(word_clean)

    matches = []

    for candidate in candidates:
        candidate_clean = candidate.lower()

        # skip same word
        if candidate_clean == word_clean:
            continue

        if sorted(candidate_clean) == sorted_word:
            matches.append(candidate)

    return matches