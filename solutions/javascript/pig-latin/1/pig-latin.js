//
// This is only a SKELETON file for the 'Pig Latin' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const translate = (text) => {
  const vowels = ['a', 'e', 'i', 'o', 'u'];

  const translateWord = (word) => {
    // Case 1: starts with vowel or "xr"/"yt"
    if (vowels.includes(word[0]) || word.startsWith("xr") || word.startsWith("yt")) {
      return word + "ay";
    }

    let consonantCluster = '';
    let i = 0;

    while (i < word.length && !vowels.includes(word[i])) {
      // Special "qu"
      if (word.startsWith("qu", i)) {
        consonantCluster += "qu";
        i += 2;
        continue;
      }

      // Special "y" (acts as vowel if not at position 0)
      if (word[i] === 'y' && i > 0) {
        break;
      }

      consonantCluster += word[i];
      i++;
    }

    return word.slice(i) + consonantCluster + "ay";
  };

  // Split sentence into words, translate each, rejoin
  return text.split(" ").map(translateWord).join(" ");
};
