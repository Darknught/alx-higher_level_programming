-- A script that list the number of records with the same score in the table
SELECT `score`, `number`
FROM `second_table`
ORDER BY `score` DESC;
