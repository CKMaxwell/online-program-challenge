// https://www.hackerrank.com/challenges/js10-function/problem?isFullScreen=true
/*
Day 1: Functions
Task
Implement a function named factorial that has one parameter: an integer, n. It must return the value of  n!(i.e., n factorial).
*/ 

function factorial(num) {
    let result = 1
    for (let i=1; i<=num; i+=1) {
        result *= i
    }
    return result;
}