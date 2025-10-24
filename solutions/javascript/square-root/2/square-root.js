//
// This is only a SKELETON file for the 'Square root' exercise. It's been provided as a
// convenience to get you started writing code faster.
//


 export const squareRoot = (number) => {
  if(number === 0 || number === 1) return number;

  let left = 1;
  let right = number;
  let ans = 0;

  while(left <= right){
    let mid = Math.floor(left + (right - left)/2);

    if(mid * mid === number){
      return mid;  // perfect square
    }
    else if(mid * mid < number){
      ans = mid;    // store the last mid whose square is <= number
      left = mid + 1;
    }
    else{
      right = mid - 1;
    }
  }

  return ans;  // integer part of sqrt
};
  

