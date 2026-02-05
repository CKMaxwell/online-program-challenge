// https://www.hackerrank.com/challenges/js10-regexp-1/problem?isFullScreen=true
// Day 7: Regular Expressions I
/*
Task
Complete the function in the editor below by returning a RegExp object, , that matches any string  that begins and ends with the same vowel. Recall that the English vowels are a, e, i, o, and u.
 */
function regexVar() {
  /*
  * Declare a RegExp object variable named 're'
  * It must match a string that starts and ends with the same vowel (i.e., {a, e, i, o, u})
  */
  let re = /^([aeiou]).*\1$/i
  
  
  /*
    * Do not remove the return statement
    */
  return re;
}
