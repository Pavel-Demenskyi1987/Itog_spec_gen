DROP DATABASE IF EXISTS HumanFriends;
CREATE DATABASE HumanFriends;
USE HumanFriends;

DROP TABLE IF EXISTS Pets;
CREATE TABLE Pets (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(45) NOT NULL,
    types VARCHAR(45) NOT NULL,
    BirthDate DATE NOT NULL,
    Commands VARCHAR(45)
);

DROP TABLE IF EXISTS PackAnimals;
CREATE TABLE PackAnimals (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(45) NOT NULL,
    types VARCHAR(45) NOT NULL,
    BirthDate DATE NOT NULL,
    Commands VARCHAR(45)
);

INSERT INTO Pets (name, types, BirthDate, Commands)
VALUES
('Fido', 'Dog', '2020-01-01', 'Sit, Stay, Fetch'),
('Whiskers', 'Cat', '2019-05-15', 'Sit, Pounce'),
('Hammy', 'Hamster', '2021-03-10', 'Roll, Hide'),
('Buddy', 'Dog', '2018-12-10', 'Sit, Paw, Bark'),
('Smudge', 'Cat', '2020-02-20', 'Sit, Pounce, Scratch'),
('Peanut', 'Hamster', '2023-08-01', 'Roll, Spin'),
('Bella', 'Dog', '2022-11-11', 'Sit, Stay, Roll'),
('Oliver', 'Cat', '2020-06-30', 'Meow, Scratch, Jump');

INSERT INTO PackAnimals (name, types, BirthDate, Commands) 
VALUES 
('Thunder', 'Horse', '2015-07-21', 'Trot, Canter, Gallop'),
('Sandy', 'Camel', '2016-11-03', 'Walk, Carry Load'),
('Eeyore', 'Donkey', '2017-09-18', 'Walk, Carry Load, Bray'),
('Storm', 'Horse', '2014-05-05', 'Trot, Canter'),
('Dune', 'Camel', '2018-12-12', 'Walk, Sit'),
('Burro', 'Donkey', '2019-01-23', 'Walk, Bray, Kick'),
('Blaze', 'Horse', '2016-02-29', 'Trot, Jump, Gallop'),
('Sahara', 'Camel', '2015-08-14', 'Walk, Run');

SELECT id, name, types, BirthDate, Commands FROM Pets;
SELECT id, name, types, BirthDate, Commands FROM PackAnimals;



DELETE FROM PackAnimals WHERE types = 'Camel';
SELECT id, name, types, BirthDate, Commands FROM PackAnimals;

-- DROP TABLE IF EXISTS YoungAnimals;
CREATE TABLE YoungAnimals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    types VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL,
    age_years INT NOT NULL
);



INSERT INTO YoungAnimals (name,types, birth_date, age_years)
SELECT 
   name,
   types,
   BirthDate, 
   TIMESTAMPDIFF(YEAR, BirthDate, CURDATE()) AS age_years
FROM 
   Pets
WHERE 
   TIMESTAMPDIFF(YEAR, BirthDate, CURDATE()) BETWEEN 1 AND 3 
   AND BirthDate <= CURDATE();
   
SELECT name,types, birth_date, age_years FROM YoungAnimals;




SELECT 
    name,
    birth_date,
    TIMESTAMPDIFF(YEAR , birth_date, CURDATE()) AS full_years,
    MONTH(CURDATE()) - MONTH(birth_date) AS month_difference
FROM 
    YoungAnimals;
    
-- DROP TABLE IF EXISTS ALL_Animals;    
CREATE TABLE ALL_Animals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    types VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL,
    full_years INT NOT NULL,
    category VARCHAR(30) NOT NULL
); 


INSERT INTO ALL_Animals (name, types, birth_date, full_years, category)
SELECT 
   name,
   types,
   BirthDate,
   TIMESTAMPDIFF(YEAR , BirthDate, CURDATE()) AS full_years,
   'Pets' AS category 
FROM 
   Pets
UNION ALL
   
SELECT 
   name,
   types,
   BirthDate,
   TIMESTAMPDIFF(YEAR , BirthDate, CURDATE()) AS full_years,   
   'PackAnimals' AS category 
FROM
	PackAnimals
UNION ALL
   
SELECT 
   name,
   types,
   birth_date, 
   age_years,
   'YoungAnimals' AS category 
FROM
	YoungAnimals;



SELECT  name, types, birth_date, full_years, category FROM ALL_Animals;








  