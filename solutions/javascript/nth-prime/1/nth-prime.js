//
// This is only a SKELETON file for the 'Nth Prime' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const prime = (n) => {
  let count=0;
  let num=1;
  if (n<1)throw new Error('there is no zeroth prime');

  while (count<n){
    num++;
  let isPrime = true;

    for (let i=2;i*i<=num;i++){
      if(num % i ===0){
        isPrime=false;
        break;
      }
    }
    if (isPrime) {
        count++;
    }
}

return num;

  
};
