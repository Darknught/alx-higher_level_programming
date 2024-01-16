--- Script that removes all records with a score <= 5 in the `second_table`
DROP `second_table`
WHERE `score` <= 5
ORDER BY `score` DESC;
