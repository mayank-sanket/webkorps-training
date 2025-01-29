-- question 8

create table employees(
emp_id serial primary key,
emp_name varchar(50),
dept_id int,
salary decimal(10,3)
);


insert into employees (emp_name, dept_id, salary) values ('Rahul', 1, 56000), ('Raj', 1, 89999), ('Ram', 2, 45000),
('Raman', 2, 40000), ('Suresh', 1, 434300), ('Ramesh', 3, 60000), ('Rohan', 4, 343433.000), ('Raghu', 4, 43000), ('Jay', 3, 70000);


create table departments(
dept_id serial,
dept_name varchar(30)
);

insert into departments (dept_name) values ('IT'), ('Finance'), ('HR'), ('Media');



select departments.dept_name, max(employees.salary), min(employees.salary), avg(employees.salary) from departments inner join employees on  departments.dept_id = employees.dept_id group by departments.dept_name;