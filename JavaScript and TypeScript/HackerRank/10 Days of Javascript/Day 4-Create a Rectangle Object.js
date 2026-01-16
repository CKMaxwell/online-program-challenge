// https://www.hackerrank.com/challenges/js10-objects/problem?isFullScreen=true
/*
Day 4: Create a Rectangle Object

Task
Complete the function in the editor. It has two parameters: a and b. It must return an object modeling a rectangle that has the following properties:

length: This value is equal to a.
width: This value is equal to b.
perimeter: This value is equal to 2(a + b) 
area: This value is equal to a * b
Note: The names of the object's properties must be spelled correctly to pass this challenge.

Input Format

The first line contains an integer denoting a.
The second line contains an integer denoting b.
*/

function Rectangle(a, b) {
  let result = {};
  result.length = a;
  result.width = b;
  result.perimeter = 2 * (a + b);
  result.area = a * b; 
  return result
}