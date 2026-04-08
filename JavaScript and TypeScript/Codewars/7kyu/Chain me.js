// Chain me
/*
Write a generic function chainer
Write a generic function chainer that takes a starting value, and an array of functions to execute on it (array of symbols for Ruby).
The input for each function is the output of the previous function (except the first function, which takes the starting value as its input). Return the final value after execution is complete.
*/
// https://www.codewars.com/kata/54fb853b2c8785dd5e000957/train/javascript
function add10(x) {
  return x + 10;
}

function mulBy30(x) {
  return x * 30;
}

function chain(input, fs) {
  if (fs == null) {
    return input;
  } else {
    let ans = input;
    for (let fun of fs) {
      ans = fun(ans);
    }
    return ans;
  }
}

console.log(chain(2, [add10, mulBy30]));
