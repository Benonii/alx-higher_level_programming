-- Displays the max temperature of each state oredered by state name
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state order by state ASC;
