//
// This is only a SKELETON file for the 'BookStore' exercise. It's been provided as a
// convenience to get you started writing code faster.
//
const discounts={
  1:0,
  2:0.05,
  3:0.1,
  4:.2,
  5:.25,
}
export const cost = (books) => {
  if(books.length ===0) return 0;

let counts=Array(5).fill(0);

  for (let book of books){
    counts[book -1]++;
  }
   let groups = [];

  while(Math.max(...counts)>0){
    let distinct =0 ;
    for(let i=0;i<counts.length;i++){
      if (counts[i]>0){
        counts[i]--;
        distinct++;
      }
        
    }
    groups.push(distinct);
  }

 while (groups.includes(5) && groups.includes(3)) {
    groups.splice(groups.indexOf(5), 1); 
    groups.splice(groups.indexOf(3), 1); 
    groups.push(4, 4);                   
  }

  
  let total = 0;
  for (let g of groups) {
    total += g * 800 * (1 - discounts[g]);
  }

 
  return total;
};
  