-- Lists the number of records witht he same score in the table second_table of the database hbtn_0c_) in your MySQL server
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
