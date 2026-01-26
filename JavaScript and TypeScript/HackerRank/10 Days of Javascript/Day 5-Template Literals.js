// https://www.hackerrank.com/challenges/js10-template-literals/problem?isFullScreen=true
/*
Day 5: Template Literals
Task
The code in the editor has a tagged template literal that passes the area and perimeter of a rectangle to a tag function named sides. Recall that the first argument of a tag function is an array of string literals from the template, and the subsequent values are the template's respective expression values.
Complete the function in the editor so that it does the following:

1. Finds the initial values of s1 and s2 by plugging the area and perimeter values into the formula:
  S = (P +- sqrt(p**2 - 16*A))/4
where A is the rectangle's area and P is its perimeter.
Creates an array consisting of s1 and s2 and sorts it in ascending order.
Returns the sorted array.
*/

function sides(literals, ...expressions) {
  let a = expressions[0];
  let p = expressions[1];
  let ans = [];
  let s1 = (p + Math.sqrt(p ** 2 - 16 * a)) / 4;
  let s2 = (p - Math.sqrt(p ** 2 - 16 * a)) / 4;
  ans.push(s1, s2)
  ans.sort();
  return ans
}
