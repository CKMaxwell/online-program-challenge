// Ho Ho Ho with Functions!
/*
Santa is learning programming. And what could be the first program, he wants to write? Yes, the "Hello world!" of Christmas: "Ho Ho Ho!". He wants to write a function ho(), which should have the following return values:

ho();         // should return "Ho!"
ho(ho());     // should return "Ho Ho!"
ho(ho(ho())); // should return "Ho Ho Ho!"
*/
// https://www.codewars.com/kata/52af1f150fcae8d33d0009bc/train/javascript
function ho(value) {
  if (value == undefined) {
    let newHo = "Ho!";
    return newHo;
  } else if (value !== undefined) {
    value = "Ho " + value;
    return value;
  }
}

console.log(ho());
console.log(ho(ho()));
