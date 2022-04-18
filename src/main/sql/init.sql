CREATE TABLE customer (
    UserName, varchar(255),
    Password, varchar(255) not null,
    LastName varchar(255) not null,
    FirstName varchar(255) not null,
    Address varchar(255)not null,
    Phone varchar(13),
    Router boolean not null,
    PRIMARY KEY (UserName)
);

insert into customer (ID, LastName, FirstName, Address, Phone, Router)
VALUES ('Woody', '1234', 'Woodard', 'Eric', '4927 test st', '555-555-5555', true);

insert into customer (ID, LastName, FirstName, Address, Phone, Router)
VALUES ('tester', 'password', 'Bobbyton', 'Bob', '3432 nonya ave', '208-123-4567', false);