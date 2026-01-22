// 35. Search Insert Position
// https://leetcode.com/problems/search-insert-position/description/?envType=problem-list-v2&envId=binary-search
/*
Time complexity:O(logn)
思路：
+ 題目是標準的binary search
+ 題目要求：沒找到的回傳值是[插入的位置]，原本判斷min的位置就是插入的位置
 */
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
  let min = 0;
  let max = nums.length - 1;
  while (min <= max) {
    mid = Math.floor((min + max) / 2);
    if (target > nums[mid]) {
      min = mid + 1;
    } else if (target < nums[mid]) {
      max = mid - 1;
    } else if (target == nums[mid]) {
        return mid
    }
  }
  return min
};
let test1 = searchInsert([1,3,5,6], 5)
let test2 = searchInsert([1,3,5,6], 2)
let test3 = searchInsert([1,3,5,6], 7)
let test4 = searchInsert([1,3], 0)
let test5 = searchInsert([1,3], 2)
console.log(test1, test2, test3, test4, test5)