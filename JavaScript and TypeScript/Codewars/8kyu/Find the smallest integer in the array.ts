// Find the smallest integer in the array
// Given an array of integers your solution should find the smallest integer.
// https://www.codewars.com/kata/55a2d7ebe362935a210000b2/train/typescript
export function findSmallestInt(args: number[]): number {
  let minValue = args[0];
  args.forEach((element) => {
    if (element < minValue) {
      minValue = element;
    }
  })
  return minValue;
}