-- A script that creates database and a table
-- id INT unique, auto generated, can’t be null and is a primary key
-- state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
  PRIVATE KEY(`id`),
  `id`       INT            NOT NULL AUTO_INCREMENT,
  `state_id` INT            NOT NULL,
  `name`     VARCHAR(256)   NOT NULL,
  FOREIGN KEY (`state_id`)
  REFRENCES `hbtn_0d_usa`.`state_id`(`id`)
);
