// https://www.hackerrank.com/challenges/js10-date/problem?isFullScreen=true
// Day 6: JavaScript Dates
/*
Given a date string, dateString, in the format MM/DD/YYYY, find and return the day name for that date. Each day name must be one of the following strings: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, or Saturday. For example, the day name for the date 12/07/2016 is Wednesday.
 */

// The days of the week are: "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
function getDayName(dateString) {
  let dayName;
  const day = new Date(dateString).getDay();
  const days = {0: "Sunday", 1: "Monday", 2: "Tueday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"};
  dayName = days[day];
  return dayName;
}
