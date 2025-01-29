-- question 1:


create table students(
s_id serial primary key,
s_name varchar(40), 
c_id int not null
);

insert into students(s_name, c_id) values('Mayank', 2), ('Rahul', 2), ('Shardul', 1), ('Raman', 3), ('Raj', 4);

create table courses(
c_id serial primary key,
c_name varchar(20) not null
);

insert into courses (c_name) values ('Physics'), ('English'), ('Computer Science'), ('Maths');


select students.s_name as Student, courses.c_name as Course from students
inner join courses on students.c_id = courses.c_id;



