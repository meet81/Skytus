--Tasks Create users table with: Primary key 
CREATE DATABASE PRIMARY_DB;
USE PRIMARY_DB;

CREATE TABLE PRMI(
USER_ID INT PRIMARY KEY,
USER_NAME VARCHAR(50),
EMAIL VARCHAR(50) UNIQUE,
PASSWORD VARCHAR(100) NOT NULL
);

CREATE TABLE ORDERS1(
ORDER_ID INT PRIMARY KEY,
USER_ID INT,
AMOUNT DECIMAL(10,2),
OrderDATE DATETIME DEFAULT GETDATE(),
FOREIGN KEY(USER_ID) REFERENCES PRMI(USER_ID)
);

INSERT INTO PRMI VALUES
(1,'MEET','m811@gmail.com',11822),
(2,'sanjay','sanjay8@gmail.com',121112),
(3,'het','het1@gmail.com',17772),
(4,'nij','nij1@gmail.com',18882),
(5,'harsh','harsh81@gmail.com',12222),
(16,'drish','drish11@gmail.com',11112)

select * from PRMI 

INSERT INTO ORDERS1 (ORDER_ID,USER_ID, AMOUNT) VALUES
(129,1,18000),
(29,2,8000),
(12,3,1000),
(19,4,1800),
(15,5,10000),
(95,16,1250)

select * from ORDERS1


--Unique email 
--Not null password 
--Add foreign key between orders and users 
--Create index on email column
create index idx_email on PRMI(email);

--Create view to display user order summary
CREATE VIEW vw_Userorders 
AS
SELECT
p.USER_ID,
p.USER_NAME,
p.EMAIL,
p.PASSWORD,
m.ORDER_ID,
m.AMOUNT
FROM PRMI p
JOIN ORDERS m
ON p.USER_ID = m.USER_ID;

select * from vw_Userorders

