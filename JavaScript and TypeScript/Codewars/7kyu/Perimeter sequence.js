// Perimeter sequence
/*
The first three stages of a sequence are shown.
The blocksize is a by a and a ≥ 1.
What is the perimeter of the nth shape in the sequence (n ≥ 1) ?
*/
// https://www.codewars.com/kata/589519d1f0902e01af000054/train/javascript
function perimeterSequence(a, n) {
  return 4 * n * a;
}

let test1 = perimeterSequence(1, 1);
let test2 = perimeterSequence(1, 3);
let test3 = perimeterSequence(2, 2);
console.log(test1, test2, test3);
