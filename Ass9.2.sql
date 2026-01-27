CREATE DATABASE STUDENT1;
USE STUDENT1;
CREATE TABLE STUDENTS(
STUDENT_ID INT,
NAME VARCHAR(30),
DEPARTMENT VARCHAR(50),
YEAR INT,
MARKS INT
);

INSERT INTO  STUDENTS VALUES
(21,'MEET','COM',4,85),
(22,'NIJ','COM',4,90),
(23,'ALAY','CHE',3,75),
(24,'PRINCE','COM',2,70),
(25,'DRISH','CHE',4,85)

--Tasks Count total number of students 
select count(*) AS total_students from STUDENTS;

--Find average marks of students 
select avg(marks) AS average_MARKS from STUDENTS;

---Find highest and lowest marks 
select MAX(MARKS) AS highest_marks, MIN(MARKS) AS lowest_marks from STUDENTS;

--Find department-wise average marks 
select department, avg(marks) as average_marks from students group by department;

--Display departments where average marks > 70	
select department, avg(marks) as average_marks from STUDENTS
where marks>70
group by department; 