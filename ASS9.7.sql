create database ecommerce;
use ecommerce;

create table customers1(
customer_id int primary key, 
name varchar(100) not null, 
city varchar(50)
);

create table orders2(
order_id int primary key, 
customer_id int, 
order_date date, 
amount decimal(10,2),
foreign key(customer_id) references customers1(customer_id)
);

create table products1(
product_id int primary key, 
product_name varchar(100) not null, 
price decimal(10,2) not null
);

create table order_items1(
order_id int, 
product_id int, 
quantity int not null,
primary key (order_id, product_id),
foreign key (order_id) references orders2(order_id),
foreign key (product_id) references products1(product_id)
);

insert into customers1 (customer_id, name, city) values
(1, 'meet', 'mumbai'),
(2, 'prince', 'valsad'),
(3, 'akshar', 'surat'),
(4, 'alay', 'ahmedabad'),
(5, 'jay', 'surat');

insert into products1 (product_id, product_name, price) values
(95, 'phone', 25000),
(12, 'laptop', 75000),
(83, 'bluetooth earbuds', 2500),
(94, 'smart watch', 1100),
(105, 'keyboard', 1500);

insert into orders2 (order_id, customer_id, order_date, amount) values
(2001, 2, '2024-01-08', 2500),
(2002, 5, '2024-01-22', 4000),
(2003, 1, '2024-02-05', 15000),
(2004, 3, '2024-02-27', 900),
(2005, 4, '2024-03-12', 6000),
(2006, 2, '2024-03-25', 7800);

insert into order_items1 (order_id, product_id, quantity) values
(2001, 95, 1),
(2001, 105, 2),
(2002, 12, 1),
(2003, 95, 1),
(2003, 83, 1),
(2004, 94, 1),
(2004, 105, 1),
(2005, 12, 1),
(2005, 94, 2),
(2006, 83, 1),
(2006, 105, 1);

select * from customers1;
select * from products1;
select * from orders2;
select * from order_items1;

SELECT * FROM orders2 WHERE order_id IN (2001,2002,2003,2004,2005,2006);

-- Total orders per customer.

select 
c.customer_id,
c.name,
count(o.order_id) as total_orders
from customers1 c
left join orders2 o
on c.customer_id = o.customer_id
group by c.customer_id, c.name;

--Customers who never placed an order.
select
c.customer_id,
c.name
from customers1 c
left join orders2 o
on c.customer_id = o.customer_id
where o.order_id is null;

-- Highest selling product.
select top 1
p.product_id,
p.product_name,
sum(oi.quantity) as total_quantity_sold
from products1 p
join order_items1 oi
on p.product_id = oi.product_id
group by p.product_id, p.product_name
order by total_quantity_sold desc;

-- Monthly sales report.

select
month(order_date) as month,
year(order_date) as year,
sum(amount) as total_sales
from orders2
group by year(order_date), month(order_date)
order by year, month;

--Customers with total purchase > ?50,000.

select
c.customer_id,
c.name,
sum(o.amount) as total_purchase
from customers1 c
join orders2 o
on c.customer_id = o.customer_id
group by c.customer_id, c.name
having sum(o.amount) > 50000;

-- Top 3 cities by revenue.
select top 3
c.city,
sum(o.amount) as total_revenue
from customers1 c
join orders2 o on c.customer_id = o.customer_id
group by c.city
order by total_revenue desc;