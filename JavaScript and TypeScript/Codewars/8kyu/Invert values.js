// Invert values
// Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
// https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/javascript
function invert(array) {
  let ans = [];
  array.forEach(element => {
    ans.push(-element)
  }); 
  return ans;
}

test1 = invert([1, -2, 3, -4, 5])
console.log(test1)