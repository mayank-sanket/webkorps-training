create table customers (
c_id serial primary key,
c_name varchar(50),
o_id int
);

insert into customers (c_name, o_id) values ('Ram', 2), ('Raj', 1), ('Raman', 6), ('John', 3), ('Jane', 4), ('Joe', 5);
insert into customers (c_name) values ('Hardik'), ('Rohit'), ('Virat');
insert into customers (c_name) values ('Rajat'), ('Akash'); -- no orders placed by them

insert into orders (o_item, o_price) values ('IPhone', 90000), ('Macbook', 100000), ('Product1', 34343), ('Product2', 23434), 
('ps5', 434343), ('xbox', 234343);



create table orders(
o_id serial primary key,
o_item varchar(50),
o_price decimal(10,2)
);


select orders.o_id, orders.o_item, orders.o_price, customers.c_id, customers.c_name from orders left join customers on orders.o_id = customers.o_id;