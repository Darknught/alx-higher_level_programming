-- A script that lists all the cities of california that can be found in database
SELECT `id`, `name`
FROM `cities`
WHERE `state_id` IN
	(SELECT `id`
	FROM `states`
	WHERE `name`. = 'California')
ORDER BY `id`;
