-- cities of california subquery
SELECT cities.id, cities.name FROM cities 
WHERE cities.state_id = 1 ORDER BY cities.id;