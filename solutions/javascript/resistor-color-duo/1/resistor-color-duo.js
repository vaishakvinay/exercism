//
// This is only a SKELETON file for the 'Resistor Color Duo' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const decodedValue = (color) => {

 const[first,second]=color;
  const firstNumber= Colors[first];
  const secondNumber=Colors[second];
  return firstNumber*10+secondNumber;

  
};
const Colors={black: 0,
brown: 1,
red: 2,
orange: 3,
yellow: 4,
green: 5,
blue: 6,
violet: 7,
grey: 8,
white: 9,
  
}