//
// This is only a SKELETON file for the 'Pangram' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const isPangram = (input) => {

 const letters= new Set(
   input.toLowerCase().split('').filter(ch=>ch>='a'&&ch<='z')
 );
  return letters.size===26;
};
