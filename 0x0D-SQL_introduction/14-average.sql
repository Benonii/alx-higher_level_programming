-- Computes the score average of all records int he table second_table of the databse hbtn_0c_0
SELECT SUM(score) / count(*) AS average FROM second_table;
