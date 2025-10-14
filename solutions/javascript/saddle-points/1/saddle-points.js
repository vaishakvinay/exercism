//
// This is only a SKELETON file for the 'Saddle Points' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const saddlePoints = (grid) => {

  let goodTrees = [];
  if (!grid || grid.length === 0 || grid[0].length === 0) {
    return [];
  }
  let numRows = grid.length;
  let numCols = grid[0].length;
for (let i=0;i<numRows;i++){
  for (let j=0;j<numCols;j++){
    let value =grid[i][j];

    let largestInRow=value;
for (let col=0;col<numCols;col++){
  if (grid[i][col]>largestInRow){
    largestInRow=grid[i][col];
     
    
  }
}
 let smallestInCol = value;
      for (let row = 0; row < numRows; row++) {
        if (grid[row][j] < smallestInCol) {
          smallestInCol = grid[row][j];

        }
        }
          if (value === largestInRow && value === smallestInCol) {
          goodTrees.push({ row: i + 1, column: j + 1 }); 
      }
    }
  }

  return goodTrees;
};
  
  