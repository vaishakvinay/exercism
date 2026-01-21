//
// This is only a SKELETON file for the 'Word Search' exercise. It's been provided as a
// convenience to get you started writing code faster.
//
class WordSearch {
  constructor(grid) {
    this.grid = grid;
  }

  find(words) {
    const grid = this.grid.map(row => row.split(''));
    const rows = grid.length;
    const cols = grid[0].length;

    const inBounds = (r, c) =>
      r >= 0 && r < rows && c >= 0 && c < cols;

    const directions = [
      [0, 1],    // right
      [0, -1],   // left
      [1, 0],    // down
      [-1, 0],   // up
      [1, 1],    // down-right
      [1, -1],   // down-left
      [-1, 1],   // up-right
      [-1, -1]   // up-left
    ];

    const results = {};

    for (const word of words) {
      let found = undefined;

      for (let r = 0; r < rows && !found; r++) {
        for (let c = 0; c < cols && !found; c++) {

          if (grid[r][c] !== word[0]) continue;

          for (const [dr, dc] of directions) {
            let match = true;
            let endRow = r;
            let endCol = c;

            for (let i = 1; i < word.length; i++) {
              const newRow = r + dr * i;
              const newCol = c + dc * i;

              if (
                !inBounds(newRow, newCol) ||
                grid[newRow][newCol] !== word[i]
              ) {
                match = false;
                break;
              }

              endRow = newRow;
              endCol = newCol;
            }

            if (match) {
              found = {
                start: [r+1, c+1],
                end: [endRow+1, endCol+1]
              };
              break;
            }
          }
        }
      }

      results[word] = found;
    }

    return results;
  }
}

export default WordSearch;
