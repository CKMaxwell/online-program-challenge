// Even or Odd
// Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
// https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/typescript
export function evenOrOdd(n:number):string {
    if (n % 2 == 0) {
        return 'Even'
    } else {
        return 'Odd'
    }
}