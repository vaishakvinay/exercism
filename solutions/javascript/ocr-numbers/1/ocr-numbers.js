//
// This is only a SKELETON file for the 'OCR Numbers' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

const DIGITS = {
  " _ | ||_|   ": "0",
  "     |  |   ": "1",
  " _  _||_    ": "2",
  " _  _| _|   ": "3",
  "   |_|  |   ": "4",
  " _ |_  _|   ": "5",
  " _ |_ |_|   ": "6",
  " _   |  |   ": "7",
  " _ |_||_|   ": "8",
  " _ |_| _|   ": "9"

};
export function convert(input) {
  let lines = input.split("\n");
  let result = "";

 
  for (let i = 0; i < lines.length; i += 4) {
    let group = lines.slice(i, i + 4);
    if (group.length < 4) continue;     

    let numCols = group[0].length;

    for (let col = 0; col < numCols; col += 3) {
      let digitStr =
        group[0].slice(col, col + 3) +
        group[1].slice(col, col + 3) +
        group[2].slice(col, col + 3) +
        group[3].slice(col, col + 3);

      result += DIGITS[digitStr] || "?";
    }

    if (i + 4 < lines.length) result += ","; 
  }

  return result;
}
