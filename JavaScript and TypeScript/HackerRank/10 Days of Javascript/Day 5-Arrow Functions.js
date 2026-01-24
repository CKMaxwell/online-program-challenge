// https://www.hackerrank.com/challenges/js10-arrows/problem?isFullScreen=true
/*
Day 5: Arrow Functions
Task
Complete the function in the editor. It has one parameter: an array, nums. It must iterate through the array performing one of the following actions on each element:

If the element is even, multiply the element by 2.
If the element is odd, multiply the element by 3.
The function must then return the modified array.
*/

function modifyArray(nums) {
  let ans = [];
  nums.forEach(element => {
    if (element % 2 == 0) {
      ans.push(element * 2)
    } else if (element % 2 != 0) {
      ans.push(element * 3)
    }
  });
  return ans;
}