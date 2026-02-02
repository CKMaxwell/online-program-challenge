// https://www.hackerrank.com/challenges/js10-bitwise/problem?isFullScreen=true
// Day 6: Bitwise Operators
/* 
Task

We define S to be a sequence of distinct sequential integers from 1 to n; in other words, S = {1,2,3...,n}. We want to know the maximum bitwise AND value of any two integers, a and b (where a < b), in sequence S that is also less than a given integer, K .
Complete the function in the editor so that given n and k, it returns the maximum a & b < k.

Note: The  symbol represents the bitwise AND operator.
*/

function getMaxLessThanK(n, k) {
  let maxValue = 0;
  for (let value1 = 1; value1 <= n; value1 += 1) {
    for (let value2 = value1 + 1; value2 <= n; value2 += 1) {
      let calValue = value1 & value2;
      if ((calValue > maxValue) && (calValue < k)) {
        maxValue = calValue;
      }
    }
  }
  return maxValue;
}


let test1 = getMaxLessThanK(5, 2);
let test2 = getMaxLessThanK(8, 5);
let test3 = getMaxLessThanK(2, 2)
console.log(test1, test2, test3)