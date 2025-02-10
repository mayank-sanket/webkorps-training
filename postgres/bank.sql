create table employees
(
emp_id serial primary key,
fname varchar(50) not null,
lname varchar(50) not null,
email varchar(100) not null unique,
dept varchar (50),
salary decimal(10) default 300000.00,
hire_date date not null default current_date
);


insert into employees (emp_id, fname, lname, email, dept, salary, hire_date) 
values
(1, 'Raj', 'Sharma', 'raj.sharma@gmail.com', 'IT', 500000.00, '2024-09-15');


insert into employees (emp_id, fname, lname, email, dept, salary, hire_date)
values
(2, 'Shyam', 'Grover', 'shyam.grover@gmail.com', 'Finance', 400000.00, '2022-08-12'),
(3, 'Raj', 'Desai', 'rdesai@gmail.com', 'HR', 300000.00, '2025-09-07');



-- let's do this: don't insert values in the emp_id column, salary column and hire_date column

insert into employees (fname, lname, email, dept)
values
('Tanya', 'Singh', 'teesingh@gmai.com', 'IT');

select * from employees;

-- if you want to do the above way, do it from the starting because of serialisation issue and primary key issue
-- (cannot set emp_id 1 again)

-- or you can do this also
-- 1. in the current database: \d employees
-- 2. in the emp_id, you will see the Default to be:  nextval('employees_emp_id_seq'::regclass)
-- 3. do this: select setval('employees_emp_id_seq', 1);    -setting the value to 1
-- 4. if you try to see this now: select currval('employees_emp_id_seq'); -- gives 1

-- 5. now to work with that, let's do this:
     -- select setval('employees_emp_id_seq', 10)

-- now if you do this:
select * from employees; -- you will see emp_id 1, 2, 3, and 11 






create table bank_employees(
emp_id serial primary key,
fname varchar(50) not null,
lname varchar(50) not null,
email varchar(100) not null unique,
dept varchar (50),
salary decimal(10) default 300000.00,
hire_date date not null default current_date
);

insert into bank_employees  (emp_id, fname, lname, email, dept, salary, hire_date) 

      VALUES

(1, 'Raj', 'Sharma', 'raj.sharma@example.com', 'IT', 50000.00, '2020-01-15'),

(2, 'Priya', 'Singh', 'priya.singh@example.com', 'HR', 45000.00, '2019-03-22'),

(3, 'Arjun', 'Verma', 'arjun.verma@example.com', 'IT', 55000.00, '2021-06-01'),

(4, 'Suman', 'Patel', 'suman.patel@example.com', 'Finance', 60000.00, '2018-07-30'),

(5, 'Kavita', 'Rao', 'kavita.rao@example.com', 'HR', 47000.00, '2020-11-10'),

(6, 'Amit', 'Gupta', 'amit.gupta@example.com', 'Marketing', 52000.00, '2020-09-25'),

(7, 'Neha', 'Desai', 'neha.desai@example.com', 'IT', 48000.00, '2019-05-18'),

(8, 'Rahul', 'Kumar', 'rahul.kumar@example.com', 'IT', 53000.00, '2021-02-14'),

(9, 'Anjali', 'Mehta', 'anjali.mehta@example.com', 'Finance', 61000.00, '2018-12-03'),

(10, 'Vijay', 'Nair', 'vijay.nair@example.com', 'Marketing', 50000.00, '2020-04-19');

select * from bank_employees;


-- CLAUSES
	-- WHERE
	-- DISTINCT
	-- ORDERY BY
	-- LIMIT
	-- LIKE

select * from bank_employees where emp_id = 5;

select * from bank_employees where dept = 'HR';

select * from bank_employees where salary < 50000;

select * from bank_employees where dept = 'HR' or dept = 'IT';
-- or
select * from bank_employees where dept in ('HR', 'IT');

select * from bank_employees where dept = 'IT' and salary >= 50000;


-- in and not in

select * from bank_employees where dept in ('HR', 'Finance', 'IT');

select * from bank_employees where dept not in ('HR', 'IT');

-- between

select * from bank_employees where salary between 40000 and 50000; -- inclusive

-- distinct

select distinct dept from bank_employees;


-- order by

select * from bank_employees order by fname;
select * from bank_employees order by salary desc;


-- limit

select * from bank_employees order by salary limit 5;

-- like

select * from bank_employees where fname like 'R%'; -- fname starting with 'R'

select * from bank_employees where fname like '%n'; --fname ends with 'n'

select * from bank_employees where fname like '%i%'; -- fname contains letter 'i' in between

select * from bank_employees where fname like '_a%' -- fname has second character 'a'

-- case insensitivity in like
select * from bank_employees where fname ilike '%rahul%' -- fname contains 'john' (case insensitive)


-- Q: find those departments which contain only 2 characters

select * from bank_employees where dept like '__';

-- Q: find those first names where the second character is 'a'

select * from bank_employees where fname like '_a%';




-- AGGREGATE FUNCTIONS
  -- COUNT
  -- SUM
  -- AVG
  -- MIN
  -- MAX

 
-- find the number of records in the table

select count(fname) from bank_employees;
-- or
select count(*) from bank_employees;
-- but prefer using primary key for that because that is not null

select count(emp_id) from bank_employees;


-- find the sum of all the salaries of employees

select sum (salary) from bank_employees;


-- find average salary of employees

select avg(salary) from bank_employees;

-- find min and max salary of employees

select min(salary) from bank_employees;

select max(salary) from bank_employees;

----------------------------------------------------------

-- GROUP BY

-- Example 1: Number of employees in each department

select dept from bank_employees group by dept; -- lists only the departments | this is not what we need

select dept, count(*) from bank_employees group by dept;
-- or
select dept, count(emp_id) from bank_employees group by dept;



-- example 2: find the total salary of each dept

select dept, sum(salary) from bank_employees group by dept;

-- ex 3: find the average salary for each dept

select dept, avg(salary) from bank_employees group by dept;


------------------------------------------------------------------------------------------------------



-- STRING FUNCTIONS

	-- CONCAT, CONCAT_WS
	-- SUBSTR
	-- LEFT, RIGHT
	-- LENGTH
	-- UPPER, LOWER
	-- TRIM, LTRIM, RTRIM
	-- REPLACE
	-- POSITION
	-- STRING_AGG


-- CONCAT

select concat('Hello', 'World'); --HelloWorld
select concat(fname, lname)  from bank_employees; -- eg RajSharma

select concat(fname, lname) as fullName from bank_employees;  -- eg RajSharma
-- or 
select concat(fname, lname) fullName from bank_employees; eg -- RajSharma


-- more variations

select emp_id, concat(fname, lname) as fullName, dept from bank_employees;


-- how to add space between firstname and lastname?

select concat(fname, ' ', lname) from bank_employees; -- not a good practice

-- use concat_ws (with separator) -- important application in CSV files

select concat_ws(' ', fname, lname) from bank_employees; -- eg Raj Sharma

------------------------------------------------------------------------
-- SUBSTRING


select substr ('Hello buddy!', 1, 4); -- Hell

select substr (fname, 1, 3) from bank_employees; -- Raj, Pri, Arj, etc


-----------------------------------------------------------------------

-- REPLACE 

select replace ('hey buddy', 'hey', 'hello') -- hello buddy

-- example replace the IT department with Tech department

select replace (dept, 'IT', 'Tech') from bank_employees; -- displays like Tech, HR, Tech and so on 

select * from bank_employees;


------------------------------------------------------------------------------

-- REVERSE

select reverse ('Hello world'); -- dlrow olleH

select reverse(lname) from bank_employees;

------------------------------------------

-- LENGTH

select length('Hello'); -- 5
select length(fname) from bank_employees;


-- q: find those entries where the first name is more than 5 characters long

select * from bank_employees where length(fname) > 5;



----------------------------------------------------------
-- UPPER and LOWER

select upper(fname) from bank_employees;
select lower(lname) from bank_employees;


----------------------------------------------------------

-- LEFT AND RIGHT

select left ('Abcdefghij', 3); -- Abc
select right ('Abcdefghij', 3); -- hij


-- TRIM
select trim ('          Abcdef      '); -- Abcdef

select length('           alright        '); -- 26
select length(trim('           alright        ')); -- 7



 -- POSITION

select position ('om' in 'Thomas'); -- 3
select position ('Om' in 'Thomas'); -- 0


--------------------------------------------------------------------

-- questions:
-- 1: display like 1:Raj:Sharma:IT

select concat_ws(':', emp_id, fname, lname, dept) from bank_employees;


-- 2: display like 1:Raj Sharma:IT:5000

select concat_ws(':', emp_id, concat_ws(' ', fname, lname), dept, salary) from bank_employees;


---------------------------------------------------------------------------------------------

-- TASKS

-- q1: display like 4:Suman:FINANCE

select concat_ws(':', emp_id, fname, upper(dept)) from bank_employees where emp_id = 4;


-- q2: display like this: I1Raj

select concat_ws('', left(dept, 1), emp_id, fname) from bank_employees;

-- q3 : display like this: 


-- other questions (easy)
-- 1: find different types of departments in the table
-- 2: display records with high-low salary
-- 3: how to see only top 3 records from the table
-- 4: show records where fname starts with 'A'
-- 5: show records where length of lname is 4

----------------------------
-- exercises: 

-- find the total no. of employees in the database:

select count(*) from bank_employees;
-- prefer using primary key as it is not null
select count(emp_id) from bank_employees;



-- find the number of employees in each department

select dept, count(dept) from bank_employees group by dept;
select dept, count(*) from bank_employees group by dept; -- this also works


-- find the lowest salary paying
select min(salary) from bank_employees;

-- find the highest salary paying
select max(salary) from bank_employees; 
-- or
select salary from bank_employees order by salary desc limit 1;


-- find the whole row where the salary is max

select * from bank_employees
where
salary =(select max(salary) from bank_employees);

-- find the total salary paying in the Finance department

select sum(salary) as total_finance_salary from bank_employees where dept = 'Finance'; -- must be 'Finance' and not'finance'


-- find the average salary paying in each department

select dept, avg(salary) from bank_employees group by dept;





-------------------------------------------------------------------------------


-- CASE Expressions

select fname, salary,
case
	when salary >= 50000 then 'High'
	when salary >= 40000 and salary <=50000 then 'Medium'   -- or : salary between 40000 and 50000
	else 'Low'
end as salary_category
from bank_employees;


-- task: add a bonus column in the table and the bonus should be 10% of the salary

select fname, salary, 
case
when salary > 0 then round(salary * 0.10) -- or simply salary * 0.10
end as bonus
from employees;

-----------------------------------------------


-- task 2 : count high, medium and low SALARY from bank_employees table

select
case
	when salary >= 50000 then 'High'
	when salary >= 40000 and salary <=50000 then 'Medium'   -- or : salary between 40000 and 50000
	else 'Low'
end as salary_category,
count (emp_id)
from bank_employees
group by salary_category;


-------------------------------------------------------------------

-- STORED ROUTINE 
-- an sql statement or a set of sql statements 
-- that can be stored on database server which can be 
-- called number of times

-- it has two types:
	-- 1. stored procedure
	-- 2. user defined functions

-- 1. STORED PROCEDURE : set of sql statements and procedural
-- logic that can perform operations such as inserting, 
-- updating, deleting, and querying data
			 
			--  syntax

			-- create or replace procedure procedure_name (parameter_name parameter_type, ...)
			-- language plpgsql
			-- as $$
			-- begin 
			     --- procedural code here
			-- end;
			-- $$;

-- eg 

create or replace procedure update_emp_salary(
	p_employee_id int,
	p_new_salary numeric
)

language plpgsql
as $$
begin
	update bank_employees
	set salary = p_new_salary
	where emp_id = p_employee_id;
end; 
$$;


-- using this stored procedure

call update_emp_salary(3, 71000);


-- task: create a stored procedure for insert operation

-- solution:

-- first create stored procedure

create or replace procedure add_employee(
	p_fname varchar,
	p_lname varchar,
	p_email varchar,
	p_dept varchar,
	p_salary numeric
)

language plpgsql
as $$
begin  
insert into bank_employees (fname, lname, email, dept, salary) 
values (p_fname, p_lname, p_email, p_dept, p_salary);
end;
$$


-- to use it, use the call keyword alongwith the name and parameters

call add_employee ('mayank', 'sanket', 'm@gmail.com', 232323.00);
-------------

-- 2. USER DEFINED FUNCTIONS: custom function created by the user to perform specific operations and return a value

		-- syntax:
		-- create or replace function function_name(parameters) 
		-- returns return_type as $$
		-- begin
		      -- fxn body (sql statements)
			-- return some_value;    (for scalar functions)
		-- end;
		-- $$ language plpgsql;




-- application of user defined function

-- eg: find the name of the employees in each department having maximum salary


create or replace function dept_max_sal_emp(dept_name varchar)
returns table(emp_id int, fname varchar, salary numeric)
as $$
BEGIN
return query
select
e.emp_id, e.fname, e.salary
from 
bank_employees e 
where e.dept = dept_name
and e.salary = (
	select max(emp.salary)
	from employees emp
	where emp.dept = dept_name
);
end;
$$ language plpgsql;


-- using the function
select * from dept_max_sal_emp('HR');




-------------------------------------------------------------------------------------------

----- WINDOW FUNCTIONS
-- window functions, also known as analytic functions allow you to perform calculations across
-- a set of of rows related to the current row

-- defined by an over() clause


-- eg:
select fname,
sum(salary) over()
from bank_employees;

-- this displays the first names in 1st col and total salary of all emp in 2nd col


select fname, salary,
sum(salary) over()
from bank_employees; -- fname, salary, total employees' salary


-- controlling over() clause

select fname, salary,
sum(salary) over(order by salary)
from bank_employees; -- fname, salary, cumulative sum of salaries in ascending order


select row_number()  over(order by fname),
fname, dept, salary
from bank_employees;



select row_nummber() over(PARTITION BY dept),   -- PARTITION BY is similar to group by when used with an over() clause
fname, dept, salary
from bank_employees; -- rows start from 1 and end to n for the same dept and again start with 1 and end to m for the other dept

-- benefits of window functions

-- Advanced Analytics: They enable complex calculations like running totals, moving averages, rank calculations, and cumulative distributions.


-- Non-Aggregating: Unlike aggregate functions, window functions do not collapse rows. This means you can calculate aggregates while retaining individual row details.


-- Flexibility: They can be used in various clauses of SQL, such as SELECT, ORDER BY, and HAVING, providing a lot of flexibility in writing queries.



-- note: other than row_number() there are many like, rank(), dense_rank(), lag(), lead()

select fname, salary,
rank() over(order by salary desc)
from bank_employees;  -- 1, 1, 3 type rank


select fname, salary,
dense__rank() over(order by salary desc)
from bank_employees; -- 1, 1, 2, 3 type rank

-- lag (peechhe)

select fname, salary,
lag(salary) over()
from bank_employees;
 -- karke dekh lo kya hota hai


select fname, salary,
lead(salary) over()
from bank_employees; -- karke dekh lo kya hota hai


---------------------------------------------------------------------------------------------


--- CTE: Common Table Expression

-- CTE (Common Table Expression) is a temporary result set that you can define within a query to simplify complex SQL statements.


-- ------------ syntax----------------
with cte_name (optional_column_list) as (
	-- cte definition
	select ...
)

-- main query referencing the cte

select ... from cte_name
where ...;


----------------



-- use case 1: 




-- We want to calculate the average salary per department and then find all employees whose salary is above the average salary of their department.


WITH AvgSal AS (

    SELECT 

        dept,  AVG(salary) AS avg_salary     FROM   bank_employees

    GROUP BY 

        dept

)



SELECT 

    e.emp_id,     e.fname,     e.dept,     e.salary, 

    a.avg_salary

FROM 

    bank_employees e

JOIN 

    AvgSal a ON e.dept = a.dept

WHERE 

    e.salary > a.avg_salary;


-- note: this is not stored

-- it is like: create cte and immediately use it

--------------------------------------------------------------------

-- Use Cases - 2



-- We want to find the highest-paid employee in each department.


WITH HighestPaid AS (

    SELECT 

        dept, 

        MAX(salary) AS max_salary

    FROM 

        bank_employees

    GROUP BY 

        dept

)

SELECT 

    e.emp_id, 

    e.fname, 

    e.lname, 

    e.desig, 

    e.dept, 

    e.salary

FROM 

    employees e

JOIN 

    HighestPaid h ON e.dept = h.dept AND e.salary = h.max_salary;



-- Points:

-- Once CTE has been created it can only be used once. It will not be persisted.
------------------------------------------------------------------------------------------------






--------------------------------------------------------------------------------------------------



-- TRIGGERS :Triggers are special procedures in a database that automatically execute predefined actions in response to certain events on a specified table or view.


-- syntax: 

create trigger trigger_name
{before | after | instead of} {insert | update | delete | truncate } 
on table_name
for each {row | statement}
execute function trigger_function_name();



-- function def

create or replace function trigger_function_name()
returns trigger as $$
BEGIN 
   -- logic here
  return new;
end;
$$ language plpgsql;




-- use case:  create a trigger so that if we insert/update negative salary in a table, it will be triggered and set it to 0


-- defining the function
create or replace function check_salary()
returns trigger as $$
BEGIN
if new.salary < 0 then
new.salary = 0;
end if;
return new;
end;
$$ language plpgsql;

-- creating the trigger

create trigger before_update_salary
before update on bank_employees
for each row
execute function check_salary();



-- let's try this by updating values in the table (this time we are using stored procedure that we earlier defined)

call update_emp_salary(1, -60000);



-- ------------------------------------------------------------------


-- more to study

--1. cascade on delete