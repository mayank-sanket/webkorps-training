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
	--WHERE
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


