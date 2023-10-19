-- Lists all cities contained in the databse hbtn_0d_usa
SELECT c.id, c.name, s.name
FROM cities c INNER JOIN states s
ON c.state_id = s.id
ORDER BY c.id;
