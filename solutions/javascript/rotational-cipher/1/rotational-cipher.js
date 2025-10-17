//
// This is only a SKELETON file for the 'Rotational Cipher' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const rotate = (text, key) => {
  let result = '';

  for (let t of text) {
    if (t >= 'A' && t <= 'Z') {
      result += String.fromCharCode((t.charCodeAt(0) - 65 + key) % 26 + 65);
    } else if (t >= 'a' && t <= 'z') {
      result += String.fromCharCode((t.charCodeAt(0) - 97 + key) % 26 + 97);
    } else {
      result += t; 
    }
  }

  return result;
};

