// Who likes it?
// You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
// Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:
// https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/typescript

export const likes = (a : string[]) : string => {
  if (a.length === 0) {
    return ("no one likes this");
  } else if (a.length === 1) {
    return (`${a[0]} likes this`);
  } else if (a.length === 2) {
    return (`${a[0]} and ${a[1]} like this`);
  } else if (a.length === 3) {
    return (`${a[0]}, ${a[1]} and ${a[2]} like this`);
  } else {
    let others = a.length - 2;
    return (`${a[0]}, ${a[1]} and ${others} others like this`);
  }
}