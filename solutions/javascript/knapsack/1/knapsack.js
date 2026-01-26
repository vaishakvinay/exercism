//
// This is only a SKELETON file for the 'Knapsack' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const knapsack = (maximumWeight, items) => {
 if (maximumWeight === 0 || items.length === 0) return 0;
   const validItems = items.filter(item => item.weight <= maximumWeight);
   if (validItems.length === 0) return 0;

  const dp = Array(maximumWeight + 1).fill(0);

  for (let item of validItems) {
    for (let w = maximumWeight; w >= item.weight; w--) {
      dp[w] = Math.max(dp[w], dp[w - item.weight] + item.value);
    }
  }

  return dp[maximumWeight];

};