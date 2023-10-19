-- Lists all the cities of California that can be found in the databse hbtn_0d_usa
SELECT * FROM cities 
WHERE cities.state_id = (SELECT id FROM cities WHERE name = "California")
ORDER BY cities.id ASC;
