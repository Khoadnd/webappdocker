CREATE DATABASE IF NOT EXISTS employee_db;
USE employee_db;

CREATE TABLE employees (name VARCHAR(20));
INSERT INTO employees VALUES ('KHOA'), ('HOANG'), ('TRUNG');

GRANT ALL ON *.* TO db_user@'%';