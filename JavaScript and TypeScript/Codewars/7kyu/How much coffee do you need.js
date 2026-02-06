// How much coffee do you need?
/*
Everybody know that you passed to much time awake during night time...

Your task here is to define how much coffee you need to stay awake after your night. You will have to complete a function that take an array of events in arguments, according to this list you will return the number of coffee you need to stay awake during day time. Note: If the count exceed 3 please return 'You need extra sleep'.

The list of events can contain the following:

You come here, to solve some kata ('cw').
You have a dog or a cat that just decide to wake up too early ('dog' | 'cat').
You just watch a movie ('movie').
Other events can be present and it will be represent by arbitrary string, just ignore this one.
Each event can be downcase/lowercase, or uppercase. If it is downcase/lowercase you need 1 coffee by events and if it is uppercase you need 2 coffees.
*/
// https://www.codewars.com/kata/57de78848a8b8df8f10005b1/train/javascript
function howMuchCoffee(events) {
  let coffeeCount = 0;
  events.forEach(element => {
    if (['cw', 'dog', 'cat', 'movie'].includes(element.toLowerCase())) {
      if (element == element.toUpperCase()) {
        coffeeCount += 2;
      } else if (element == element.toLowerCase()) {
        coffeeCount += 1;
      }
    }
  })
  if (coffeeCount > 3) {
    return 'You need extra sleep';
  } else {
    return coffeeCount
  }
}

let test1 = howMuchCoffee(['cw']);
let test2 = howMuchCoffee(['CW']);
let test3 = howMuchCoffee(['cw','CAT', 'cw=others']);
let test4 = howMuchCoffee(['cw','CAT','DOG']);
console.log(test1, test2, test3, test4)