//
// This is only a SKELETON file for the 'All Your Base' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const convert = (digits, inputBase, outputBase) => {
  if (inputBase < 2) throw new Error('Wrong input base');
  if (outputBase < 2) throw new Error('Wrong output base');

  if (
    digits.length === 0 ||
    (digits.length > 1 && digits[0] === 0) ||
    digits.some(d => d < 0 || d >= inputBase)
  ) {
    throw new Error('Input has wrong format');
  }

 
  let decimal = 0;
  for (let d of digits) {
    decimal = decimal * inputBase + d;
  }


  if (decimal === 0) return [0];

  const outputDigits = [];
  while (decimal > 0) {
    outputDigits.unshift(decimal % outputBase);
    decimal = Math.floor(decimal / outputBase);
  }

  return outputDigits;
};

 