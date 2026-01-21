// Return Negative
// In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?
// https://www.codewars.com/kata/55685cd7ad70877c23000102/train/typescript
export const makeNegative = (num: number): number => {
  if (num < 0) {
    return num;
  } else {
    return num * (-1);
  }
};