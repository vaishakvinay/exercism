//
// This is only a SKELETON file for the 'Anagram' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const findAnagrams = (word, candidates) => {
  const wordLower = word.toLowerCase();
  const sortedWord = wordLower.split('').sort().join('');
  const anagrams = [];

  for (const candidate of candidates) {
    const candidateLower = candidate.toLowerCase();
    
    if (candidateLower === wordLower) {
      continue; // skip the same word
    }

    const sortedCandidate = candidateLower.split('').sort().join('');
    if (sortedCandidate === sortedWord) {
      anagrams.push(candidate); // push the original candidate
    }
  }

  return anagrams;
};
