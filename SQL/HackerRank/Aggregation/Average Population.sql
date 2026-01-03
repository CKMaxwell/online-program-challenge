-- Average Population
-- Query the average population for all cities in CITY, rounded down to the nearest integer.
-- https://www.hackerrank.com/challenges/average-population/problem
SELECT 
    ROUND(AVG(population), 0) AS avg_population
FROM city;