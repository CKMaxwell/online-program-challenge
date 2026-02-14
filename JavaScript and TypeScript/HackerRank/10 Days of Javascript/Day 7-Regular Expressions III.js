// https://www.hackerrank.com/challenges/js10-regexp-3/problem?isFullScreen=true
// Day 7: Regular Expressions III
/*
Task
Complete the function in the editor below by returning a RegExp object, re, that matches every integer in some string s.
*/
function regexVar() {
  /*
   * Declare a RegExp object variable named 're'
   * It must match ALL occurrences of numbers in a string.
   */
  const re = /([0-9]+)/g;

  /*
   * Do not remove the return statement
   */
  return re;
}
