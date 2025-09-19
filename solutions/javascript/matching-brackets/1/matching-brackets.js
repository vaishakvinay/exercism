//
// This is only a SKELETON file for the 'Matching Brackets' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const isPaired = (input) => {
  const stack = [];
  const pairs = {'(': ')', '[': ']', '{': '}'};

  for (const char of input) {
    if ("([{".includes(char)) {
      stack.push(pairs[char]);  // push expected closing bracket
    } else if (")]}".includes(char)) {
      if (stack.pop() !== char) {
        return false;
      }
    }
  }

  return stack.length === 0;
};


