//
// This is only a SKELETON file for the 'Rectangles' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export function count(input) {
  let rectangles = 0;

  // loop over rows
  for (let i = 0; i < input.length; i++) {
    // pick first '+'
    for (let j1 = 0; j1 < input[i].length; j1++) {
      if (input[i][j1] !== '+') continue;

      // look for second '+' on same row
      for (let j2 = j1 + 1; j2 < input[i].length; j2++) {
        if (input[i][j2] !== '+') continue;

        // Now we have two '+' on row i → potential top edge
        // scan downward for bottom edge
        for (let k = i + 1; k < input.length; k++) {
          // check vertical edges at j1 and j2
          if ((input[k][j1] !== '+' && input[k][j1] !== '|') ||
              (input[k][j2] !== '+' && input[k][j2] !== '|')) {
            break; // invalid edge, stop searching downwards
          }

          // found a bottom edge
          if (input[k][j1] === '+' && input[k][j2] === '+') {
            // check if all middle cells between j1 and j2 are '-' or '+'
            let validTop = true;
            for (let x = j1 + 1; x < j2; x++) {
              if (input[i][x] !== '-' && input[i][x] !== '+') {
                validTop = false;
                break;
              }
            }
            let validBottom = true;
            for (let x = j1 + 1; x < j2; x++) {
              if (input[k][x] !== '-' && input[k][x] !== '+') {
                validBottom = false;
                break;
              }
            }

            if (validTop && validBottom) {
              rectangles++;
            }
          }
        }
      }
    }
  }

  return rectangles;
};