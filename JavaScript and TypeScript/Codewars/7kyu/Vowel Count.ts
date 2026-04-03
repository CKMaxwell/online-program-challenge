// Vowel Count
/*
Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.
*/
// https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/typescript
export class Kata {
  static getCount(str: string): number {
    let num = 0;
    for (let i = 0; i < str.length; i += 1) {
      if (["a", "e", "i", "o", "u"].includes(str[i])) {
        num += 1;
      }
    }
    return num;
  }
}
