// https://www.hackerrank.com/challenges/js10-count-objects/problem?isFullScreen=true
/* 
Day 4: Count Objects
Task
Complete the function in the editor. It has one parameter: an array, a, of objects. 
Each object in the array has two integer properties denoted by x and y. 
The function must return a count of all such objects o in array a that satisfy o.x == o.y .
 */

function getCount(objects) {
  let count_ans = 0;
  objects.forEach(element => {
    if (element.x == element.y) {
      count_ans += 1;
    }
  });
  return count_ans;
}