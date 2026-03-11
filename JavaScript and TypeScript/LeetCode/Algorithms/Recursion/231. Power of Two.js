// 231. Power of Two
/*
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2^x.
*/
// https://leetcode.com/problems/power-of-two/?envType=problem-list-v2&envId=recursion
var isPowerOfTwo = function (n) {
  // console.log(n);
  if (n === 1) {
    return true;
  } else if (n < 1) {
    return false;
  }
  return isPowerOfTwo(n / 2);
};

console.log(isPowerOfTwo(17));
