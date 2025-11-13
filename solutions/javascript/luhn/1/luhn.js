//
// This is only a SKELETON file for the 'Luhn' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const valid = (input) => {

  let cleaned=input.replaceAll(' ','');
  if (!/^\d+$/.test(cleaned)){return false;}
if(cleaned.length<=1)return false;
  
let arr = cleaned.split('').reverse();
  for (let i = 1; i < arr.length; i += 2) {
    let digit=Number(arr[i])*2;


    if(digit>9){
      digit-=9;
    }
    arr[i]=digit;
  }
  let sum=arr.reduce((total,x)=>total+Number(x),0);
  return sum%10 ==0;
};
