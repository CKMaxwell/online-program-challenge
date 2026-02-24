// Sort Out The Men From Boys
// https://www.codewars.com/kata/5af15a37de4c7f223e00012d/train/typescript
export function menFromBoys(arr: number[]): number[] {
  let boy = [];
  let man = [];
  for (let element of arr) {
    if (element % 2 == 0) {
      boy.push(element);
    } else {
      man.push(element);
    }
  }
  boy.sort((a, b) => a - b);
  man.sort((a, b) => b - a);
  let uniqueBoy = [...new Set(boy)];
  let uniqueMan = [...new Set(man)];
  let ans = uniqueBoy.concat(uniqueMan);
  return ans;
}
