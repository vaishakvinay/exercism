//
// This is only a SKELETON file for the 'Sublist' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class List {
  constructor(array=[]) {
    this.items=array;
  }

  compare(other) {
    if (
      this.items.length === other.items.length &&
      this.items.every((val, index) => val === other.items[index])
    ) {
      return "EQUAL";
    }
    if( this.items.length < other.items.length &&
        this.isSublistOf(other)){
      return "SUBLIST"
    }
        if( this.items.length > other.items.length &&
        other.isSublistOf(this)){
      return "SUPERLIST"
    }
    return "UNEQUAL";
  }
isSublistOf(other) {
  return other.items.some((_, startIndex) =>
    this.items.every(
      (val, i) => val === other.items[startIndex + i]
    )
  );
}
  
}
