//
// This is only a SKELETON file for the 'High Scores' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class HighScores {
  constructor(array) {
    this.highScore=array;
  }

  get scores() {
    return this.highScore;
  }

  get latest() {
    return this.highScore.at(-1);
  }

  get personalBest() {
    return Math.max(...this.highScore);
  }
  get personalTopThree() {
  return [...this.highScore]
  .sort((a, b) => b - a)
  .slice(0, 3);
  }
}
