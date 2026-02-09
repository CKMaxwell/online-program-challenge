// Sum of odd numbers
/*
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) 
*/
// https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/javascript

function rowSumOddNumbers(n) {
  let totoalAmount = ((1 + n) * n) / 2;
  let maxNumber = totoalAmount * 2 - 1;
  let result = 0;
  for (let i = 0; i < n; i += 1) {
    result += maxNumber - i * 2;
  }
  return result;
}

let test1 = rowSumOddNumbers(2);
let test2 = rowSumOddNumbers(42);
console.log(test1, test2);
