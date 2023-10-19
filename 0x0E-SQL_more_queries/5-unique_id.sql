-- Creates the table unique_id with id habving a default value of 1 and being unique
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
