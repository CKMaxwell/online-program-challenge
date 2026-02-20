// Sum Arrays
/*
Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative. If the array is empty, return 0.
*/
// https://www.codewars.com/kata/53dc54212259ed3d4f00071c/train/javascript

function sum(numbers) {
  let ans = 0;
  for (const value of numbers) {
    ans += value;
  }
  return ans;
}

console.log(sum([1, 5.2, 4, 0, -1]));
