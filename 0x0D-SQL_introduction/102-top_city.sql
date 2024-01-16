-- A script that displays top 3 cities tempearture during july and August ordered by temp
SELECT `city`, AVG(`value`) AS `max_temp`
FROM `temperatures`
WHERE MONTH(date) IN (7, 8)
GROUP BY `city`
ORDER BY `max_temp` DESC
LIMIT 3;
