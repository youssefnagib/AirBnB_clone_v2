-- create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- user privilages over hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- user select privilage over performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- save changes
FLUSH PRIVILEGES;
