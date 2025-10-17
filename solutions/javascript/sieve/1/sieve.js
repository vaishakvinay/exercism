//
// This is only a SKELETON file for the 'Sieve' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const primes = (n) => {
  let result = [];

  for (let i = 2; i <= n; i++) {
    let isPrime = true;

    for (let j = 2; j * j <= i; j++) {
      if (i % j === 0) {
        isPrime = false;
        break;
      }
    }

  
    if (isPrime) {
      result.push(i);
    }
  }

  return result;
};
