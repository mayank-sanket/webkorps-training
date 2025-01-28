create table person(
id int, 
name varchar(100),
city varchar(100)
);




-- ALTER QUERIES




alter table person
add column age int; -- adds one column age with int data type

select * from person; -- displays all data (age is null)
alter table person
drop column age; -- removes the age column


alter table person
add column age int default 0;

select * from person


-- how to rename a column?

alter table person 
rename column name to fname;


-- how to rename a table?

alter table person
rename to people;


-- how to modify a column? eg changing data type or adding default values etc


-- changing data type of a column
alter table people 
alter column fname
set data type varchar(200);


-- setting default value in a column
alter table people
alter column fname
set default 'unknown';


-- removing default value from a column

alter table people
alter column fname
drop default;


-- setting not null

alter table people
alter column fname
set not null;




-----------------------------------------------------------

-- CHECK CONSTRAINT

-- eg: make sure the contact number is at least 10 digit long

-- first add a column for phone number


alter table people
add column
	mob varchar(15) default 1234567890 check (length(mob) >= 10);


-- how to verify?

-- insert into people(mob) values(12323); --error
insert into people(mob, fname) values (1234567890, 'test');

-- deleting this row again
delete from people where fname = 'test';


-- extras:
-- alter table people drop constraint mob_no_less_than_10digits;
-- alter table people add constraint mob_not_null check (mob != null);


-- dropping the constraint

alter table people drop constraint people_mob_check;


insert into people(id, fname, city, mob) values(7, 'test', 'test', 13131); -- this works as the constraint is removed now
select * from people;



-- named constraint
-- syntax:

create table contacts(
name varchar (50),
mob varchar(15) unique not null,
constraint mob_ check(length(mob) >=10)
);
