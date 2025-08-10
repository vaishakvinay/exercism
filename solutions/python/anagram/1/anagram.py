def find_anagrams(word, candidates):
    word_lower = word.lower()
    sorted_word = sorted(word_lower)
    anagrams = []

    for candidate in candidates:
        candidate_lower = candidate.lower()
        if candidate_lower == word_lower:
            continue  # skip same word
        if sorted(candidate_lower) == sorted_word:
            anagrams.append(candidate)  # keep original case

    return anagrams

