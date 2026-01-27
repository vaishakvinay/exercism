//
// This is only a SKELETON file for the 'Rail Fence Cipher' exercise. It's been provided as a
// convenience to get you started writing code faster.
//
export const encode = (input, rail) => {
  if (!input) return '';
  let spaceRemoved = input.replace(/\s+/g, '');
  let rows = Array(rail).fill('');
  let currentRow = 0;
  let goingDown = false;

  for (let char of spaceRemoved) {
    rows[currentRow] += char;

    if (currentRow === 0 || currentRow === rail - 1) {
      goingDown = !goingDown;
    }

    currentRow += goingDown ? 1 : -1;
  }

  return rows.join('');
};

export const decode = (cipher,rail) => {
   if (!cipher) return '';
  // Step 1: Build the zigzag pattern for each character position
  let pattern = [];
  let currentRow = 0;
  let goingDown = false;

  for (let i = 0; i < cipher.length; i++) {
    pattern.push(currentRow);
    if (currentRow === 0 || currentRow === rail - 1) {
      goingDown = !goingDown;
    }
    currentRow += goingDown ? 1 : -1;
  }

  
  let railLengths = Array(rail).fill(0);
  for (let i = 0; i < pattern.length; i++) {
    railLengths[pattern[i]]++;
  }


  let railsArray = [];
  let index = 0;
  for (let r = 0; r < rail; r++) {
    railsArray[r] = cipher.slice(index, index + railLengths[r]);
    index += railLengths[r];
  }


  let positions = Array(rail).fill(0);
  let decoded = '';

  for (let i = 0; i < pattern.length; i++) {
    let railIndex = pattern[i];
    decoded += railsArray[railIndex][positions[railIndex]];
    positions[railIndex]++;
  }

  return decoded;
};

