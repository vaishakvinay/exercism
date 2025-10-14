//
// This is only a SKELETON file for the 'Diamond' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const rows = (input) => {
  let result = [];

  
  let count = input.charCodeAt(0) - 'A'.charCodeAt(0) + 1;

  
  for (let i = 1; i <= count; i++) {
   
    let outerSpaces = ' '.repeat(count - i);

    
    let innerSpaces;
    if (i === 1) {
      innerSpaces = ''; 
    } else {
      innerSpaces = ' '.repeat((i - 1) * 2 - 1);
    }

   
    let letter = String.fromCharCode('A'.charCodeAt(0) + i - 1);

   
    let line;
    if (i === 1) {
      line = outerSpaces + letter + outerSpaces;
    } else {
      line = outerSpaces + letter + innerSpaces + letter + outerSpaces;
    }

    result.push(line);
  }

  
  for (let i = count - 1; i >= 1; i--) {
    result.push(result[i - 1]);
  }

  return result;
};


  
  


