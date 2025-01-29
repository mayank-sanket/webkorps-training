create table customers(
id serial primary key, 
name varchar(40)
);

insert into customers (name) values ('aman'), ('rajan'), ('harsh'), ('adarsh'), ('amrit'), ('mayank');

create table orders(
id serial primary key,
price decimal(10, 3),
cust_id int
);




insert into orders (price, cust_id) values (100, 2), (300, 3), (500, 4), (600, 1), (500, 3);

select  customers.name as name , sum(orders.price) as individual_sale from orders inner join customers on orders.cust_id = customers.id group by customers.id;

select count(*) from orders;