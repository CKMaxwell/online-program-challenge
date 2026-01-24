// 69. Sqrt(x)
/*
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
*/
// https://leetcode.com/problems/sqrtx/description/?envType=problem-list-v2&envId=binary-search
/*
時間複雜度 O(log(n))
思路-1st AC：
- 假設存在一個[1~target]的數列，使用binary search進行
- 把原始的mid 大於/小於 traget改成 mid**2
與原始binary search的調整
- 考慮極端情況：target = 1 or 0，high不能自動聰明，寫成x-1
- 為了符合題目要求的[sqrt向下找整數]，接著回顧high/low於終止的意義
  - high: 第一個「大於 target」的位置（insertion position）
  - low: 最後一個「小於 target」的位置
  - 故應該回傳high
調整-2nd AC：
- 修改if順序以增加效率
*/

/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
  let low = 0;
  let high = x;
  while (low <= high) {
    mid = Math.floor((low + high) / 2);
    if (x == mid * mid) {
      return mid
    } else if (x > mid * mid) {
      low = mid + 1;
    } else if (x < mid * mid) {
      high = mid -1;
    }
  }
  return high
};

let test1 = mySqrt(4);
let test2 = mySqrt(8);
let test3 = mySqrt(1);
let test4 = mySqrt(0);
console.log(test1, test2, test3, test4)