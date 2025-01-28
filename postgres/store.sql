
create table customers(
cust_id serial primary key,
cust_name varchar(100) not null
);

create table orders(
ord_id SERIAL primary key, 

            ord_date DATE not null, 

            price NUMERIC not null,

            cust_id INTEGER not null, 

            foreign key (cust_id) references 

            customers (cust_id) 
);


-- note: if you do \d customers in shell then you see something like cust_id references ..... etc





INSERT INTO customers (cust_name)

VALUES 

    ('Raju'), ('Sham'), ('Paul'), ('Alex');


INSERT INTO orders (ord_date, cust_id, price)

VALUES 

    ('2024-01-01', 1, 250.00),  

    ('2024-01-15', 1, 300.00),  

    ('2024-02-01', 2, 150.00),

    ('2024-03-01', 3, 450.00),

    ('2024-04-04', 2, 550.00);  


-- join operation is used to combine rows from two or more
-- tables based on a related column between them

-- types of joins:

	--cross join
	-- inner join
	-- left join
	-- right join

-- cross join :  every row from one table is combined with every row from another table

select * from customers cross join orders; -- not much useful



-- inner join : returns only the rows where there is a match between the 
-- specified columns in both the left (or the first) and the right (or the second) tables

select * from customers c
inner join orders o
on c.cust_id = o.cust_id;



-- inner join with group by
select c.cust_name, count(o.ord_id) from customers c
inner join 
orders o
on c.cust_id = o.cust_id
group by cust_name;   -- displays the total orders by people

select c.cust_name, sum(o.price) from customers c
inner join 
orders o
on c.cust_id = o.cust_id
group by cust_name;  -- displays the total order value by people




-- left join : returns all rows from the left table (first table) 
-- and the matching rows from the right (or the second) table

select * from customers c
 left join
 orders o

 on c.cust_id = o.cust_id; -- note: still shows the row with Alex data (even though he has no orders => all values except id and name are null)
 



select * from customers c
 right join
 orders o

 on c.cust_id = o.cust_id;


 -- try this:

 select * from orders o
 right join
 customers c

 on c.cust_id = o.cust_id; -- shows row correspoding to Alex also (even though he has no orders) because it is right join