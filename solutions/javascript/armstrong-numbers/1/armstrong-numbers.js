//
// This is only a SKELETON file for the 'Armstrong Numbers' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const isArmstrongNumber = (number) => {
number = BigInt(number);
let result=0n;
let numStr=number.toString();
let numLen=BigInt(numStr.length);

  for(let i=0;i<numLen;i++){
  result+=BigInt(numStr[i])**numLen; 
  }
 return result===number; 
};
