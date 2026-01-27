//
// This is only a SKELETON file for the 'Scrabble Score' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

const letter={
  1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
  2: ["D", "G"],
  3: ["B", "C", "M", "P"],
  4: ["F", "H", "V", "W", "Y"],
  5: ["K"],
  8: ["J", "X"],
  10: ["Q", "Z"]}



export const score = (input) => {
  let result = 0;
  input = input.toUpperCase();
  for (let i of input) {
    for (let [key, values] of Object.entries(letter)) {
      if (values.includes(i)) {
        result += Number(key);
        break;
      }
    }
  }
  return result;
};

