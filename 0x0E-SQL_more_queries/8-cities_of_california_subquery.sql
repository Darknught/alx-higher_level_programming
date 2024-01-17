-- A script that lists all the cities of california that can be found in database
SELECT `cities`.`id`, `cities`.`name`
FROM `cities`, `states`
WHERE `cities`.`state_id` = `states`.`id`
	And `states`.`name`. = 'California'
ORDER BY `cities`.`id` ASC;
