// https://www.hackerrank.com/challenges/js10-try-catch-and-finally/problem?isFullScreen=true
/*
Day 3: Try, Catch, and Finally
Task
Complete the reverseString function; it has one parameter, s. You must perform the following actions:
1. Try to reverse string s using the split, reverse, and join methods.
2. If an exception is thrown, catch it and print the contents of the exception's message on a new line.
3. Print s on a new line. If no exception was thrown, then this should be the reversed string; if an exception was thrown, this should be the original string.

*/

function reverseString(s) {
    try {
        let reverseStr = s.split('').reverse().join('')
        console.log(reverseStr);
    } catch(e) {
        console.log(e.message);
        console.log(s);
    }
}