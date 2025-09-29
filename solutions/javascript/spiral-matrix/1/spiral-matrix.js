//
// This is only a SKELETON file for the 'Spiral Matrix' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const spiralMatrix = (size) => {
let n=size;
let matrix = [];
for (let i = 0; i < n; i++) {
  matrix.push(Array(n).fill(0));
}
let left = 0, right = n - 1;
let top = 0, bottom = n - 1;
let num = 1;

 while (left <= right && top <= bottom) {
   for (let i = left; i <= right; i++) {
  matrix[top][i] = num;
  num++;
}
top++;
   for (let i = top; i <= bottom; i++) {
  matrix[i][right] = num;
  num++;
}
right--;
  if (top <= bottom) {
    for (let i = right; i >= left; i--) {
      matrix[bottom][i] = num;
      num++;
    }
    bottom--;
  }

  
  if (left <= right) {
    for (let i = bottom; i >= top; i--) {
      matrix[i][left] = num;
      num++;
    }
    left++;
  }
}

return matrix;
};
