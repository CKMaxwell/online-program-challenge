// Factorial
/*
Your task is to write function factorial.
*/
// https://www.codewars.com/kata/57a049e253ba33ac5e000212/train/javascript

function factorial(num) {
  if (num == 0) {
    return 1;
  } else if (num == 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

console.log(factorial(0));
