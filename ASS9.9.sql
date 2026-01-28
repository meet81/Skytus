CREATE DATABASE employee;
use employee;

create table employee1(
name varchar(50),
employee_id int,
salary int,
hire_date date
);

insert into employee1 VALUES
('MEET',811,80000,'2025-08-01'),
('JAY',111,60000,'2025-06-05'),
('PRINCE',880,70000,'2025-05-21'),
('NIJ',901,40000,'2025-11-11'),
('ALAY',221,30000,'2025-12-01')

SELECT * FROM EMPLOYEE1;

create table employee1_DUB(
name varchar(50),
employee_id int,
salary int,
);
insert into employee1_DUB VALUES
('MEET',811,80000),
('JAY',111,60000),
('PRINCE',880,70000),
('NIJ',901,40000),
('ALAY',221,30000)
SELECT * FROM EMPLOYEE1_DUB;

CREATE TABLE LOGS(
ID INT,
VALUE INT
);

INSERT INTO LOGS VALUES
(1,50),
(2,60),
(3,50),
(4,70),
(5,50),
(6,60),
(7,60);

SELECT * FROM LOGS

--Write query to find Nth highest salary 
SELECT salary
FROM (
SELECT salary,
DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
FROM employee1
) t
WHERE rnk = 1;
 
--Remove duplicate records 
ALTER TABLE EMPLOYEE1
ADD CONSTRAINT UQ_EMPLOYEE1 UNIQUE (NAME);

SELECT * FROM employee1

--Find records common in two tables 
SELECT a.*
from employee1 a
inner join employee1_DUB b
on a.employee_id = b.employee_id ;
--Find employees hired in last 6 months 
SELECT * FROM employee1
WHERE hire_date >= DATEADD(MONTH, -6 , GETDATE());

--Find continuous duplicate values	
select distinct value
from(select value, lag(value) over (order by id) as prev_value from logs)t
where value = prev_value

