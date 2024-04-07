-- a script that creates the database hbtn_0d_usa and the table cities
SELECT id, name
FROM city
WHERE state_id = (SELECT id FROM `state` WHERE `name` = 'California')
ORDER BY id ASC;
