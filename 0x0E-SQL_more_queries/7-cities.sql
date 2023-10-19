-- Creates the database hbtn_0d_use and the table cities (int he database hbtn_0d_usa on my server
CREATE DATABASE IF NOT EXISTS hbtn_d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT PRIMARY KEY,
	state_id INT,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
	);
