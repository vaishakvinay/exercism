//
// This is only a SKELETON file for the 'Run Length Encoding' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const encode = (str) => {
  let result='';
  let count=1;


  for (let ch in str) {
    if (str[ch] === str[parseInt(ch) + 1]) {
      count = count + 1;
    } else {
      if (count > 1) {
        result = result + count + str[ch];
      } else {
        result = result + str[ch];
      }
      count = 1; 
    }
  }

  return result;
};

export const decode = function(str) {
  let result = '';
  let num = '';

  for (let ch of str) {
    if (ch >= '0' && ch <= '9') {
      num += ch;  
    } else {
    
      let count = num ? parseInt(num, 10) : 1;
      result += ch.repeat(count);
      num = '';
    }
  }

  return result;
}


