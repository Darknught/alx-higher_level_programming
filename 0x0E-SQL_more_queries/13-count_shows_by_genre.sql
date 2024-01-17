-- Script that lists all genres from hbtn_0d_tvshows and displas the number of shows linked to each other
SELECT g.`genre` AS `genre`, COUNT(s.`id`) AS `number_of_shows`
FROM `tv_show_genre` g
JOIN `tv_shows` s ON g.`show_id` = s.`id`
GROUP BY g.`genre`
ORDER BY `number_of_show`s DESC;
