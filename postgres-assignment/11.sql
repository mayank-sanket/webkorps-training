create table products(
id serial primary key,
name varchar (50),
price decimal(10,3), 
categ_id int
);

create table category(
id serial primary key,
name varchar(50)

);

insert into category (name) values ('computers'), ('mobiles'), ('books'), ('sports');
insert into products(name, price, categ_id) values ('macbook', 100000, 1), ('samsung galaxy', 40000, 2), ('cengage', 500, 3),
('dell', 50000, 1), ('redmi', 12000, 2), ('atomic habits', 300, 3), ('bat', 2000, 4);

select c.name, max(p.price)as max_price_cat from category as c left join products as p on c.id = p.categ_id group by c.name;
