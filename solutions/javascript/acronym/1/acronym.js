//
// This is only a SKELETON file for the 'Acronym' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const parse = (str) => {
   const words = str.toLowerCase().replace(/[-|_]/g, " ").split(" ");
  let acr = "";
    for (const w of words) {
      if (w.length === 0) continue; 
    acr+=w[0].toUpperCase();
  }
  return acr;
};
