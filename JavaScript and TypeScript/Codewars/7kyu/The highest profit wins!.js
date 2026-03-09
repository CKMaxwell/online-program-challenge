// The highest profit wins!
/*
Task
Write a function that returns both the minimum and maximum number of the given list/array.
*/
// https://www.codewars.com/kata/559590633066759614000063/train/javascript
function minMax(arr) {
  let maxValue = Math.max(...arr);
  let minValue = Math.min(...arr);
  return [minValue, maxValue];
}
console.log(minMax([1, 2, 3, 4, 5]));
