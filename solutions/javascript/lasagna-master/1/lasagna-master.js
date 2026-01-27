/// <reference path="./global.d.ts" />
// @ts-check

/**
 * Implement the functions needed to solve the exercise here.
 * Do not forget to export them so they are available for the
 * tests. Here an example of the syntax as reminder:
 *
 * export function yourFunction(...) {
 *   ...
 * }
 */
export function cookingStatus(input){

  if (input===0) return 'Lasagna is done.';
  else if(input > 0) return 'Not done, please wait.';
    else return 'You forgot to set the timer.';
  
}
export function preparationTime(layers,time=2){
  return layers.length*time;
} 
export function quantities(layers){
  let noodles = 0;
  let sauce=0;
  for(let layer of layers){
    if(layer==='sauce') sauce+=0.2;
    else if(layer==='noodles') noodles+=50;
  }
    return {noodles:noodles, sauce:sauce};
}
export function addSecretIngredient(friendsList, myList){

let item = friendsList.at(-1);
  myList.push(item);
}
export function scaleRecipe(recipe,portions) {
const newRecipe = {};
  for(let items in recipe){
  newRecipe[items] =(recipe[items]/2)*portions;
  }
  return newRecipe;
};