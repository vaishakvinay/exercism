//
// This is only a SKELETON file for the 'Pythagorean Triplet' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

class Triplet {
  constructor(a, b, c) {
    this.a = a;
    this.b = b;
    this.c = c;
  }
  toArray() {
    return [this.a, this.b, this.c];
  }
}
export function triplets({ minFactor = 1, maxFactor, sum }) {
  const result = [];
  
  for (let a = minFactor; a < sum / 3; a++) {
    const num = (sum * sum) - (2 * sum * a);
    const d = (2 * sum) - (2 * a);
    
    if (num % d === 0) {
      const b = num / d;
      const c = sum - a - b; 
      if (b > a) {
        const meetsMax = !maxFactor || (b <= maxFactor && c <= maxFactor);
        
        if (meetsMax) {
          result.push(new Triplet(a, b, c));
        }
      }
    }
  }
  return result;
}


