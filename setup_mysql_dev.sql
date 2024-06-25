-- create database
CREATE  DATABASE IF NOT EXISTS hbnb_dev_db;

-- create user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- user  PRIVILEGES over hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- user select privileges over performance_schema
GRANT SELECT on performance_schema.* TO 'hbnb_dev'@'localhost';
-- save changes
FLUSH PRIVILEGES;
