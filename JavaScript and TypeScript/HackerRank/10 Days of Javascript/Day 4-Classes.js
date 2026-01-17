// https://www.hackerrank.com/challenges/js10-class/problem?isFullScreen=true
/*
Day 4: Classes
Task

Create a Polygon class that has the following properties:

A constructor that takes an array of integer values describing the lengths of the polygon's sides.
A perimeter() method that returns the polygon's perimeter.
Locked code in the editor tests the Polygon constructor and the perimeter method.

Note: The perimeter method must be lowercase and spelled correctly.
*/

class Polygon {
  constructor(side) {
    this.side = side;
  }
  perimeter() {
    let total = 0;
    this.side.forEach(element => {
        total += Number(element)
    });
    return total;
  }
}