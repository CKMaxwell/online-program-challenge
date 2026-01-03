-- Revising the Select Query II
-- Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.
-- https://www.hackerrank.com/challenges/revising-the-select-query-2/problem?isFullScreen=true
SELECT 
    c.name
FROM city AS c
WHERE population > 120000
AND countrycode = 'USA'