// Clean up after your dog
/*
You have stumbled across the divine pleasure that is owning a dog and a garden. Now time to pick up all the cr@p! :D
Given a 2D array to represent your garden, you must find and collect all of the dog cr@p - represented by '@'.
You will also be given the number of bags you have access to (bags), and the capactity of a bag (cap). If there are no bags then you can't pick anything up, so you can ignore cap.
You need to find out if you have enough capacity to collect all the cr@p and make your garden clean again.
If you do, return 'Clean', else return 'Cr@p'.
Watch out though - if your dog is out there ('D'), he gets very touchy about being watched. If he is there you need to return 'Dog!!'.
*/
// https://www.codewars.com/kata/57faa6ff9610ce181b000028/train/javascript

function crap(x, bags, cap){
  let capSum = bags * cap;
  for (const row of x) {
    for (const ground of row) {
      if (ground == 'D') {
        return 'Dog!!';
      } else if (ground == '@') {
        capSum -= 1;
      }
    }
  }
  if (capSum < 0) {
    return 'Cr@p';
  } else if (capSum >= 0) {
    return 'Clean'
  }
}

ans = crap([['_','_','_','_'], ['_','_','_','@'], ['_','_','@', '_']], 1, 1)
console.log(ans)