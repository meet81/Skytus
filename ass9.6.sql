--Tasks Start a transaction 
create database bank;
use bank;

create table acc(
acc_name varchar(50),
acc_no int,
amount int,
)
insert into acc values
('meet',1134,90000),
('het',1234,80000),
('nij',2234,70000),
('sanjay',4434,75000),
('alay',3334,85000)

select * from acc 

--Insert record into accounts 
begin transaction;
insert into acc (acc_name,acc_no,amount)
values('prince',4545,72000)

--Rollback changes 
rollback;
select * from acc

begin transaction;
insert into acc (acc_name,acc_no,amount)
values('prince',4545,72000)
--Commit valid transactions 
commit;
select * from acc
begin transaction;
insert into acc (acc_name,acc_no,amount)
values('jay',455,75000)
rollback;
select * from acc
--Demonstrate transfer of money using transaction
update acc set amount=amount-15000
where acc_no= 4545
select * from acc

begin transaction;
insert into acc (acc_name,acc_no,amount)
values('henil',45,60000)

commit;
update acc set amount=amount+5000
where acc_no= 45
select * from acc

UPDATE acc
SET acc_name = 'sanjay'
WHERE acc_no=45;
select * from acc
