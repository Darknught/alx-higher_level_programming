-- Script that updates the score of Bob to 10 in second_table
SELECT `name`
FROM `second_table`
UPDATE 'Bob' TO 10
ORDER BY `score` DESC;
