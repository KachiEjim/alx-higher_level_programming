USE hbtn_0c_0;
SOURCE temperatures.sql;

SELECT `city`, AVG(`value`) AS avg_temp
FROM `temperatures`
WHERE `month` IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
