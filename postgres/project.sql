-- TASK STORE DB

-- customers
create table customers(
cust_id serial primary key,
cust_name varchar(50) not null
);

-- orders

create table orders(
ord_id serial primary key,
ord_date date not null,
cust_id integer not null,
foreign key (cust_id) references customers(cust_id)
);


-- products

create table products(
p_id serial primary key,
p_name varchar(50) not null,
price numeric not null
);

-- items
create table order_items(
item_id serial primary key,
ord_id integer not null,
p_id integer not null,
quantity integer not null,
foreign key(ord_id) references orders (ord_id),
foreign key (p_id) references products (p_id)
);



----------------   inserting values ----------------------------------------------

insert into customers(cust_name) values 
('Raju'), ('Sham'), ('Paul'), ('Alex');


insert into orders(ord_date, cust_id) values
('2024-01-01', 1), -- Raju made first order
('2024-02-01', 2), -- Sham made first order
('2024-03-01', 3), -- Paul made first order
('2024-04-01', 2); -- Sham made second order


insert into products(p_name, price) values
('Laptop', 55000.00), 
('Mouse', 500),
('Keyboard', 800),
('Cable', 250);


insert into order_items(ord_id, p_id, quantity) values
(1, 1, 1), -- Raju ordered 1 laptop
(1, 4, 2), -- Raju ordered 2 cables
(2, 1, 1), -- Sham ordered 1 laptop
(3, 2, 1); -- Paul ordered 1 mouse


-------------------------------------------------------------------------------------------------------
select p.p_name, p.price, oi.quantity, o.ord_date, c.cust_name, (oi.quantity * p.price) total_price from order_items oi
join products p on oi.p_id = p.p_id
join orders o on o.ord_id = oi.ord_id
join customers c on o.cust_id = c.cust_id;




--- to do : create a table which shows the bill for each user (do later)






----------------------------------CONCEPT OF VIEWS -------------------------
-- views are used for frequently used queries (stores the query only and not the data)
-- if the data is updated later, it will not reflect in the view

create view billing_info as 
select p.p_name, p.price, oi.quantity, o.ord_date, c.cust_name, (oi.quantity * p.price) total_price from order_items oi
join products p on oi.p_id = p.p_id
join orders o on o.ord_id = oi.ord_id
join customers c on o.cust_id = c.cust_id;

-- using views

select * from billing_info;




-- task: find the total/revenue generated from each item of each items 

select p_name, sum(total_price) from billing_info
group by p_name;



------- HAVING CLAUSE ------
-- this is used in those cases when you have to apply a condition where you have used 'group by' | cannot use 'where'

select p_name, sum(total_price) from billing_info
group by p_name
having sum(total_price) >= 500;




------------------- GROUP BY ROLLUP -----------------------------
-- find total sale

select p_name, sum(total_price) total_p from billing_info
GROUP BY rollup (p_name) order by total_p; -- the last row will have p_name set to null and total_p equal to total sale


-- better syntax
select coalesce (p_name, 'TOTAL'),
sum(total_price) as amount
from billing_info
group by rollup (p_name) order by amount;