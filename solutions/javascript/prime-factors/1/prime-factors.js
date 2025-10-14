//
// This is only a SKELETON file for the 'Prime Factors' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const primeFactors = (n) => {
  let result=[];

  for (let i = 2; i <= n; i++) {
    while (n % i === 0) {
      result.push(i); // store the prime factor
      n /= i;        // reduce n
    }
  }


  return result;
};
