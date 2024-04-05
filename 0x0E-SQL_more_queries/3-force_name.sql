--  a script that creates the force_name table in your MySQL server
CREATE TABLE IF NOT EXISTS force_name (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
);
