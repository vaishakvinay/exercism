//
// This is only a SKELETON file for the 'Isogram' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const isIsogram = (str) => {
 const word = str.toLowerCase().replace(/[-\s]/g, "");
  const seen = new Set();

  for (const ch of word) {
    if (seen.has(ch)) return false;
    seen.add(ch);
  }

  return true;
};
  
