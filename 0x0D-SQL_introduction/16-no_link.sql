-- A script that lists all records of the table 
-- Results are displayed in descending order
-- Dosnt list rows without a name value
SELECT * FROM `second_table`
WHERE `name` IS NOT NULL
ORDER BY `score` DESC;

