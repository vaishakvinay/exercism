//
// This is only a SKELETON file for the 'Queen Attack' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class QueenAttack {
  constructor({
    black: [blackRow, blackColumn] = [0,3],
    white: [whiteRow, whiteColumn] = [7,3],
  } = {}) {

  const isOnBoard = (row, col) =>
    row >= 0 && row < 8 && col >= 0 && col < 8;

  if (!isOnBoard(whiteRow, whiteColumn) || !isOnBoard(blackRow, blackColumn)) {
    throw new Error('Queen must be placed on the board');
  }

  if (whiteRow === blackRow && whiteColumn === blackColumn) {
    throw new Error('Queens cannot share the same space');
  }

  this.white = [whiteRow, whiteColumn];
  this.black = [blackRow, blackColumn];
}
toString() {
  let board = [];
  for (let row = 0; row < 8; row++) {
    let line = [];
    for (let col = 0; col < 8; col++) {
      if (this.white[0] === row && this.white[1] === col) line.push('W');
      else if (this.black[0] === row && this.black[1] === col) line.push('B');
      else line.push('_');
    }
    board.push(line.join(' '));
  }
  return board.join('\n');

  }

  get canAttack() {
  const [wRow, wCol] = this.white;
  const [bRow, bCol] = this.black;

  // Same row → horizontal attack
  if (wRow === bRow) return true;

  // Same column → vertical attack
  if (wCol === bCol) return true;

  // Same diagonal → diagonal attack
  if (Math.abs(wRow - bRow) === Math.abs(wCol - bCol)) return true;

  // Otherwise, no attack possible
  return false;
}
}
