// First Fibonacci
/*The challenge
Your challenge is, given two numbers in a Fibonacci-like sequence (where the next number is found by adding the two previous numbers), to find the lowest possible non-negative numbers that the sequence originates from. For example, if you are given the numbers 398 and 644, which come from this sequence:

2, 6, 8, 14, 22, 36, 58, 94, 152, 246, 398, 644
Then you would return 2 and 6, as they are the numbers which started the sequence.

Note that 8 and 14, while they also start a sequence containing 398 and 644, are not correct as they are not the lowest possible sequence start.
 */
// https://www.codewars.com/kata/6965d769930fb2eff921668f/train/javascript
function solution(first,second) {
  let temp = second - first;
  if (first - temp < 0) {
    return [ first, second ];
  } else {
    second = first;
    first = temp;
    while (first - (second - first) >= 0) {
        temp = second - first;
        second = first;
        first = temp;
    } 
    return [ first, second ];
  }
}

result = solution(398,644);
console.log(result);