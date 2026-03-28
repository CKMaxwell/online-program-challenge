// Maximum Length Difference
/*
You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. Let x be any string in the first array and y be any string in the second array.

Find max(abs(length(x) − length(y)))

If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).
*/
// https://www.codewars.com/kata/5663f5305102699bad000056/train/javascript

function mxdiflg(a1, a2) {
  let x_max = -Infinity;
  let x_min = Infinity;
  let y_max = -Infinity;
  let y_min = Infinity;
  if (a1.length == 0 || a2.length == 0) {
    return -1;
  } else {
    for (let i = 0; i < a1.length; i += 1) {
      if (a1[i].length > x_max) {
        x_max = a1[i].length;
      }
      if (a1[i].length < x_min) {
        x_min = a1[i].length;
      }
    }
    for (let j = 0; j < a2.length; j += 1) {
      if (a2[j].length > y_max) {
        y_max = a2[j].length;
      }
      if (a2[j].length < y_min) {
        y_min = a2[j].length;
      }
    }
  }
  console.log(x_max, x_min, y_max, y_min);
  let ans = Math.max(Math.abs(x_max - y_min), Math.abs(y_max - x_min));
  return ans;
}

var s1 = [
  "hoqq",
  "bbllkw",
  "oox",
  "ejjuyyy",
  "plmiis",
  "xxxzgpsssa",
  "xxwwkktt",
  "znnnnfqknaz",
  "qqquuhii",
  "dvvvwz",
];
var s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"];
console.log(mxdiflg(s1, s2));
