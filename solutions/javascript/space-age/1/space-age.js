//
// This is only a SKELETON file for the 'Space Age' exercise. It's been provided as a
// convenience to get you started writing code faster.
//
const planet={mercury	:0.2408467,
venus	:0.61519726,
earth	:1.0,
mars	:1.8808158,
jupiter	:11.862615,
saturn	:29.447498,
uranus	:84.016846,
neptune	:164.79132,};
export const age = (planetToCheck,ageInSeconds) => {
  if (!(planetToCheck in planet)) {
    throw new Error('not a planet');
  }

  const result = ageInSeconds / (31557600 * planet[planetToCheck]);
  return Math.round(result * 100) / 100;
};
