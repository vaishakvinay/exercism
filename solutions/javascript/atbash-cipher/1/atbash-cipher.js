//
// This is only a SKELETON file for the 'Atbash Cipher' exercise. It's been provided as a
// convenience to get you started writing code faster.
//
const isAlpha = (char) => /^[a-z]$/.test(char);
const isDigit = (char) => /^[0-9]$/.test(char);

export const encode = (text) => {
  let t = text.toLowerCase();
  let encoded = '';

  for (let i = 0; i < t.length; i++) {
    if (isAlpha(t[i])) {
      encoded += String.fromCharCode('z'.charCodeAt(0) - (t.charCodeAt(i) - 97));
    } else if (isDigit(t[i])) {
      encoded += t[i];
    }
    // ignore punctuation and spaces
  }

  const cleaned = encoded.replace(/\s+/g, '');
  let grouped = '';

  for (let i = 0; i < cleaned.length; i += 5) {
    grouped += cleaned.slice(i, i + 5) + ' ';
  }

  return grouped.trim();
};


export const decode = (ciphertext) => {
 let t = ciphertext.toLowerCase();
  let decoded = '';

  for (let i = 0; i < t.length; i++) {
    if (isAlpha(t[i])) {
      decoded += String.fromCharCode('z'.charCodeAt(0) - (t.charCodeAt(i) - 97));
    } else if (isDigit(t[i])) {
      decoded += t[i];
    }
    
  }
  return decoded
};
