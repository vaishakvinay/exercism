//
// This is only a SKELETON file for the 'Strain' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const keep = (collection,predicate) => {
  let result=[];

  for (let element of collection){
    if(predicate(element)){
      result.push(element)
    }
  }
  return result;
};

export const discard = (collection,predicate) => {
   let result=[];

  for (let element of collection){
    if(!predicate(element)){
      result.push(element)
    }
  }
  return result;

};
