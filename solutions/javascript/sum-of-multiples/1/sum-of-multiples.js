//
// This is only a SKELETON file for the 'Sum Of Multiples' exercise. It's been provided as a
// convenience to get you started writing code faster.

export function getMultiples(n, limit) {
  let multiples = [];
  if (n === 0) return multiples;

  let current = n;
  while (current < limit) {
    multiples.push(current);
    current += n;
  }
  return multiples;
}


export const sum = (points, limit) => {
  let res = new Set(); 

  for (let n of points) {
    let multiples = getMultiples(n, limit);
    for (let m of multiples) {
      res.add(m);
    }
  }

  return [...res].reduce((a, b) => a + b, 0);
};






