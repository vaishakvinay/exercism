
export class InvalidInputError extends Error {
  constructor(message) {
    super();
    this.message = message || 'Invalid Input';
  }
}


export class Robot {
 
  #x = 0;        
  #y = 0;         
  #direction = 'north'; 
  
  get bearing() {
    return this.#direction;
  }

  
  get coordinates() {
    return [this.#x, this.#y];
  }

  
  place({ x, y, direction }) {
    const validDirections = ['north', 'south', 'east', 'west'];
    if (!validDirections.includes(direction)) {
      throw new InvalidInputError('Invalid direction');
    }
    this.#x = x;
    this.#y = y;
    this.#direction = direction;
  }

 
  turnRight() {
    const directions = ['north', 'east', 'south', 'west'];
    const currentIndex = directions.indexOf(this.#direction);
    this.#direction = directions[(currentIndex + 1) % 4];
  }


  turnLeft() {
    const directions = ['north', 'west', 'south', 'east'];
    const currentIndex = directions.indexOf(this.#direction);
    this.#direction = directions[(currentIndex + 1) % 4];
  }

  
  advance() {
    switch (this.#direction) {
      case 'north':
        this.#y += 1;
        break;
      case 'south':
        this.#y -= 1;
        break;
      case 'east':
        this.#x += 1;
        break;
      case 'west':
        this.#x -= 1;
        break;
    }
  }

 
  evaluate(instructions) {
    for (const ch of instructions) {
      switch (ch) {
        case 'R':
          this.turnRight();
          break;
        case 'L':
          this.turnLeft();
          break;
        case 'A':
          this.advance();
          break;
        default:
          throw new InvalidInputError(`Invalid instruction: ${ch}`);
      }
    }
  }
}


