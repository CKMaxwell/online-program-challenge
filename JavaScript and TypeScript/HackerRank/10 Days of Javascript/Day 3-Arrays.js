// https://www.hackerrank.com/challenges/js10-arrays/problem?isFullScreen=true
/* Day 3: Arrays
Function Description

Complete the getSecondLargest function in the editor below.

getSecondLargest has the following parameters:
int nums[n]: an array of integers

Returns
int: the second largest number in nums

Input Format
The first line contains an integer, n, the size of the nums array.
The second line contains n space-separated numbers that describe the elements in nums.
 */

function getSecondLargest(nums) {
    nums.sort((a, b) => b - a);
    let largestNum = nums[0];
    let SecondLargestNum = nums[0];
    for (let i = 0; i < nums.length; i += 1) {
        if (nums[i] < largestNum) {
            SecondLargestNum = nums[i];
            return SecondLargestNum;
        }
    }
}
