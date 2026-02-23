// Square(n) Sum
/*
Complete the square sum function so that it squares each number passed into it and then sums the results together.
*/
// https://www.codewars.com/kata/515e271a311df0350d00000f/train/typescript
export function squareSum(numbers: number[]): number {
  let ans = 0;
  for (let element of numbers) {
    ans += element ** 2;
  }
  return ans;
}
