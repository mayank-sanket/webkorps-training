create table items(
item_id serial,
item_name varchar(50)
);

insert into items(item_name) values ('notebooks'), ('bags'), ('pencils'), ('mouse');


create table vendors(
vendor_id serial,
vendor_name varchar(50),
item_id int
);


insert into vendors(vendor_name, item_id) values ('mayank', 1), ('sanket', 1), ('rahul', 2), ('raman', 4);
insert into vendors (vendor_name) values ('raj'), ('rakesh');

select * from vendors left join items on vendors.item_id = items.item_id;