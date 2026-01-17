-- Lists all cities of California found in the database
-- Uses a subquery instead of a JOIN
SELECT id, name FROM cities 
WHERE state_id = (SELECT id FROM states WHERE name = 'California') 
ORDER BY id ASC;
