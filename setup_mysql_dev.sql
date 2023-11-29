-- prepare_mysql.sql

-- Creating the database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creating a new user with password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Giving all privileges to the new user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Giving SELECT privileges to new user on 'performance_schema' database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- forces the server to re-read the grant tables and apply these changes immediately.
FLUSH PRIVILEGES;
