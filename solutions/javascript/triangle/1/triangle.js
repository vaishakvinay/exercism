//
// This is only a SKELETON file for the 'Triangle' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class Triangle {
  constructor(...sides) {
    const[a,b,c]=sides;
    this.a=a;
    this.b=b;
    this.c=c;
  }
get isValid() {
    const { a, b, c } = this;
    const allSidesPositive = a > 0 && b > 0 && c > 0;
    const satisfiesInequality = (a + b >= c) && (b + c >= a) && (a + c >= b);
    return allSidesPositive && satisfiesInequality;
  }
  get isEquilateral() {
     if (!this.isValid) return false;
    return this.a===this.b && this.b===this.c && this.a != 0;
  }

  get isIsosceles() {
     if (!this.isValid) return false;
    return this.a===this.b || this.b===this.c || this.c===this.a;
  }

  get isScalene() {
     if (!this.isValid) return false;
    return this.a !== this.b && this.b !== this.c && this.c !== this.a; 
  }
}
