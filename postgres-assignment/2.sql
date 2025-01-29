-- question 2

create table employees(
emp_id serial primary key,
emp_name varchar(60) not null,
dept_id int
);

create table departments(
dept_id serial primary key,
dept_name varchar(20) not null
);


insert into employees(emp_name, dept_id) values ('Milton', 2), ('John', 3), ('Jack', 4), ('Joe', 5);
insert into employees(emp_name) values ('Mayank'), ('Sanket'), ('Naval'), ('Ravikant');
insert into departments (dept_name) values ('IT'), ('Finance'), ('HR'), ('Media'), ('Cultural'), ('Innovation'), ('Research');

select * from employees left join departments on  departments.dept_id = employees.dept_id;

select e.emp_id, e.emp_name, e.dept_id, d.dept_name from employees e left join departments d on e.dept_id = d.dept_id;