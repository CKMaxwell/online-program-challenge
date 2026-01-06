// https://www.hackerrank.com/challenges/js10-loops/problem?isFullScreen=true
/* Day 2: Loops
Task
First, print each vowel in s on a new line. The English vowels are a, e, i, o, and u, and each vowel must be printed in the same order as it appeared in s.
Second, print each consonant (i.e., non-vowel) in s on a new line in the same order as it appeared in s. 
*/
function vowelsAndConsonants(s) {
    for (let i = 0; i < s.length; i += 1) {
        if (['a', 'e', 'i', 'o', 'u'].includes(s[i])) {
            console.log(s[i]);
        }
    }
    for (let i = 0; i < s.length; i += 1) {
        if (!['a', 'e', 'i', 'o', 'u'].includes(s[i])) {
            console.log(s[i]);
        }
    }
}