-- A script that creates unique_id on MySQL server
CREATE TABLE IF NOT EXIST `unique_id` (
  id INT DEFAULT 1 UNIQUE,
  name VARCHAR(256)
);
