-- question 4: 

create table authors (
auth_id serial primary key,
auth_name varchar(60)
);


insert into authors (auth_name) values ('Ankur Warikoo'), ('Chetan Bhagat'), ('Joseph Murphy'), ('JB Peterson'), ('Elon Musk');


create table books(
book_id serial primary key,
auth_id int not null,
book_name varchar(60)
);

insert into books (auth_id, book_name) values (1, 'Book1'), (2, 'Book 2'), (3, 'Book 3'), (4, 'book 4'), (5, 'book 5'), (1, 'book 6')
, (1, 'book 8'), (1, 'book 11'), (3, 'book 98'), (4, 'book 65');


select authors.auth_id, authors.auth_name, books.book_name from authors inner join books on books.auth_id = authors.auth_id order by authors.auth_id;


