//
// This is only a SKELETON file for the 'Flower Field' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const annotate = (garden) => {
  if (!garden || garden.length === 0) return [];

  let result = [];

  for (let row = 0; row < garden.length; row++) {
    let newRow = "";

    for (let col = 0; col < garden[row].length; col++) {
      if (garden[row][col] === "*") {
        newRow += "*";
      } else {
        let count = 0;

        // check all 8 directions
        for (let i = -1; i <= 1; i++) {
          for (let j = -1; j <= 1; j++) {
            if (i === 0 && j === 0) continue; // skip self
            let r = row + i;
            let c = col + j;

            if (r >= 0 && r < garden.length && c >= 0 && c < garden[r].length) {
              if (garden[r][c] === "*") count++;
            }
          }
        }

        newRow += count > 0 ? count.toString() : " ";
      }
    }

    result.push(newRow);
  }

  return result;
};
