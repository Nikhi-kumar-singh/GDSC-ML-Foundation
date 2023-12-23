CREATE DATABASE IF NOT EXISTS company;
USE company;


CREATE TABLE customer1 (
	id INT PRIMARY KEY,
    name VARCHAR(20),
    mode VARCHAR(20)
);
DROP TABLE customer2;
CREATE TABLE customer2 (
	id INT PRIMARY KEY,
    name VARCHAR(20),
	city VARCHAR(20)
);


INSERT INTO customer1
(id,name,mode)
VALUES
(101,"olivia barette","netbanking"),
(102,"ethan sinclair","credit card"),
(103,"maya hamandez","credit card"),
(104,"liam donovan","netbanking"),
(105,"sophia nguyen","credit card"),
(106,"caleb foster","debit card"),
(107,"ava patel","debit card"),
(108,"lucas carter","netbanking"),
(109,"isabella martinez","netbanking"),
(110,"jackson brooks","credit card"),
(111,"jackeje brooks","credit card"),
(112,"jackson broddhd","credit card");

INSERT INTO customer2
(id,name,city)
VALUES
(101,"olivia barette","portland"),
(102,"ethan sinclair","miami"),
(103,"maya hamandez","seattle"),
(104,"liam donovan","denver"),
(105,"sophia nguyen","new orleans"),
(106,"caleb foster","minneapolis"),
(113,"maya hamandez","seattle"),
(114,"liam donovan","denver"),
(115,"sophia nguyen","new orleans"),
(116,"caleb foster","minneapolis");


SELECT * FROM customer1;
SELECT * FROM customer2;

SELECT c1.id,c1.name,c1.mode,c2.city 
FROM customer1 as c1
INNER JOIN customer2  as c2
ON c1.id=c2.id;

SELECT *
FROM customer1 as c1
INNER JOIN customer2  as c2
ON c1.id=c2.id;

SELECT c1.id,c1.name,c1.mode,c2.city 
FROM customer1 as c1
left JOIN customer2  as c2
ON c1.id=c2.id;

SELECT c1.id,c1.name,c1.mode,c2.city 
FROM customer1 as c1
RIGHT JOIN customer2  as c2
ON c1.id=c2.id;


SELECT c1.id,c1.name,c1.mode,c2.city 
FROM customer1 as c1
left JOIN customer2  as c2
ON c1.id=c2.id
UNION
SELECT c1.id,c1.name,c1.mode,c2.city 
FROM customer1 as c1
RIGHT JOIN customer2  as c2
ON c1.id=c2.id;


SELECT *
FROM customer1 as c1 
left JOIN customer2 as c2
ON c1.id=c2.id
WHERE c2.id IS NULL;


SELECT *
FROM customer1 as c1 
RIGHT JOIN customer2 as c2
ON c1.id=c2.id
WHERE c1.id IS NULL;


SELECT *
FROM customer1 as c1 
left JOIN customer2 as c2
ON c1.id=c2.id
WHERE c2.id IS NULL
UNION
SELECT *
FROM customer1 as c1 
RIGHT JOIN customer2 as c2
ON c1.id=c2.id
WHERE c1.id IS NULL;


SELECT *
FROM customer1 as c1 
JOIN customer1 as c2
ON c1.id=c2.id ;

SELECT *
FROM customer1 as c1 
INNER JOIN customer1 as c2
ON c1.id=c2.id ;


DROP DATABASE IF EXISTS company;
