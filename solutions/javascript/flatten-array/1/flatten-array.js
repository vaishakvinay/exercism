//
// This is only a SKELETON file for the 'Flatten Array' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const flatten = (iterables) => {
  let result=[];

  const helper =(arr)=>{
    for(let el of arr){
      if(el === null||el === undefined)continue;
      if(Array.isArray(el)){
        helper(el);
      }
      else{result.push(el);}
    }
  };
  
  helper(iterables)
  return result;
  };
