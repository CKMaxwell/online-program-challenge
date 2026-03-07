// Three added Characters
/*
Given two strings, the first being a random string and the second being the same as the first, but with three added characters somewhere in the string (three same characters),

Write a function that returns the added character

You can assume that string2 will aways be larger than string1, and there will always be three added characters in string2.
*/
// https://www.codewars.com/kata/5971b219d5db74843a000052/train/javascript

function addedChar(s1, s2) {
  let counter1 = {};
  let counter2 = {};
  for (let i = 0; i < s1.length; i += 1) {
    if (!(s1[i] in counter1)) {
      counter1[s1[i]] = 1;
    } else if (s1[i] in counter1) {
      counter1[s1[i]] += 1;
    }
  }
  for (let j = 0; j < s2.length; j += 1) {
    if (!(s2[j] in counter2)) {
      counter2[s2[j]] = 1;
    } else if (s2[j] in counter2) {
      counter2[s2[j]] += 1;
    }
    if (!(s2[j] in counter1)) {
      return s2[j];
    } else if (counter2[s2[j]] > counter1[s2[j]]) {
      return s2[j];
    }
  }
}

let str1 = "hello";
let str2 = "checlclo";
console.log(addedChar(str1, str2));
