CREATE TABLE IF NOT EXISTS full_passengers(
  id INT, 
  pclass INT, 
  survived INT, 
  pname VARCHAR(100), 
  sex VARCHAR(50), 
  age INT,
  sibsp INT, 
  parch INT,
  ticket VARCHAR(100),
  fare DECIMAL(10, 2),
  cabin VARCHAR(50), 
  embarked VARCHAR(50),
  boat VARCHAR(50),
  body INT,
  homedest VARCHAR(100)
);
LOAD DATA INFILE '/var/lib/mysql-files/titanic_full_data.csv'
INTO TABLE full_passengers
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id, pclass, survived, pname, sex, @age, sibsp, parch, ticket, @fare, cabin, embarked, boat, @body, homedest)
SET 
  age = NULLIF(@age,''), 
  fare = NULLIF(@fare, ''), 
  body = NULLIF(@body, '');
