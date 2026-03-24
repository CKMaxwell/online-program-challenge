// Sum Factorial
/*
Factorials are often used in probability and are used as an introductory problem for looping constructs. In this kata you will be summing together multiple factorials.
*/
// https://www.codewars.com/kata/56b0f6243196b9d42d000034/train/javascript

function factorial(num) {
  if (num == 0) {
    return 1;
  } else if (num == 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

function sumFactorial(arr) {
  let ans = 0;
  for (let num of arr) {
    ans += factorial(num);
  }
  return ans;
}

console.log(sumFactorial([4, 6]));
