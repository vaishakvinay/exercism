//
// This is only a SKELETON file for the 'Pascals Triangle' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const rows = (n) => {
  const triangle = [];

  for (let row = 0; row < n; row++) {
    triangle[row] = [1];

    for (let col = 1; col < row; col++) {
      triangle[row][col] = triangle[row - 1][col - 1] + triangle[row - 1][col];
    }

    if (row > 0) triangle[row].push(1);
  }

  // optional: print to console
  for (let row = 0; row < n; row++) {
    const spaces = ' '.repeat(n - row - 1);
    const numbers = triangle[row].join(' ');
    console.log(spaces + numbers);
  }

  return triangle; // ← important!
};
