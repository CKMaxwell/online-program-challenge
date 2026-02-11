// Product of Largest Pair
/*
Rick wants a faster way to get the product of the largest pair in an array. Your task is to create a performant solution to find the product of the largest two integers in an array of positive numbers.
*/
// https://www.codewars.com/kata/5784c89be5553370e000061b/train/javascript

function maxProduct(a) {
  let first = -Infinity;
  let second = -Infinity;
  for (let i = 0; i < a.length; i += 1) {
    if (a[i] > first) {
      second = first;
      first = a[i];
    } else if (a[i] > second) {
      second = a[i];
    }
  }
  return first * second;
}

let test1 = maxProduct([154, 428, 455, 346]);
let test2 = maxProduct([
  39, 135, 47, 275, 37, 108, 265, 457, 2, 133, 316, 330, 153, 253, 321, 411,
]);
let test3 = maxProduct([136, 376, 10, 146, 105, 63, 234]);
console.log(test1, test2, test3);
