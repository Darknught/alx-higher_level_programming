-- A script that displays average tempearture(farenheit) by city ordered by temp
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `ang_temp` DESC;
