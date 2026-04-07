// A Rule of Divisibility by 7
// https://www.codewars.com/kata/55e6f5e58f7817808e00002e/train/javascript

function seven(m) {
  let count = 0;
  function forLargeSeven(num) {
    if (num < 100) {
      return [num, count];
    } else {
      count += 1;
      let inputTxt = String(num);
      let firstTxt = inputTxt.slice(0, -1);
      let lastTxt = inputTxt[inputTxt.length - 1];
      let newNumber = Number(firstTxt) - 2 * Number(lastTxt);
      return forLargeSeven(newNumber);
    }
  }
  return forLargeSeven(m);
}

console.log(seven(371));
