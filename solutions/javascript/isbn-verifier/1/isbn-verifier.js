//
// This is only a SKELETON file for the 'ISBN Verifier' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const isValid = (input) => {
  // Remove all hyphens
  let filtered = input.split("-").join("");

  // ISBN-10 must be exactly 10 characters
  if (filtered.length !== 10) {
    return false;
  }

  let sum = 0;

  for (let i = 0; i < filtered.length; i++) {
    const char = filtered[i];
    let num;

    // Last character can be 'X' which counts as 10
    if (i === 9 && char === 'X') {
      num = 10;
    } else {
      num = Number(char);
      // If it's not a number, invalid input
      if (isNaN(num)) return false;
    }

    // Weighted sum: multiply by position weight (10 to 1)
    sum += num * (10 - i);
  }

  // Valid if sum is divisible by 11
  return sum % 11 === 0;
};
