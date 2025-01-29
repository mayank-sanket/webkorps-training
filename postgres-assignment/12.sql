create table orders(
id serial primary key,
name varchar(50),
qty int
);

insert into orders(name, qty) values ('macbook', 1), ('iphone', 2), ('glasses', 3), ('bags', 11), ('airpods', 17);

select orders.id, orders.qty as QUANTITY from orders;