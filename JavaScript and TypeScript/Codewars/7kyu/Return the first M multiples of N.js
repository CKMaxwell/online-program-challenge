// Return the first M multiples of N
/*
Implement a function that takes two numbers m and n and returns an array of the first m multiples of the real number n. Assume that m is a positive integer.
*/
// https://www.codewars.com/kata/593c9175933500f33400003e/train/javascript
function multiples(m, n){
  let ans = [];
  for (let i = 1; i <= m; i += 1) {
    ans.push(n * i);
  }
  return ans;
}