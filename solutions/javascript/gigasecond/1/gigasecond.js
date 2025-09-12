//
// This is only a SKELETON file for the 'Gigasecond' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const gigasecond = (date) => {
  const giga=(10**9)*1000;
  const result= date.getTime()+giga;
  return new Date(result)
};
