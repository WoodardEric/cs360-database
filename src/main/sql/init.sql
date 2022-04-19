CREATE TABLE customer (
    Email varchar(255),
    Password varchar(255) not null,
    LastName varchar(255) not null,
    FirstName varchar(255) not null,
    Address varchar(255)not null,
    Phone varchar(13),
    Router boolean not null,
    PRIMARY KEY (Email)
);

insert into customer (Email, Password, LastName, FirstName, Address, Phone, Router)
VALUES ('Wood@test.com', '1234', 'Woodard', 'Eric', '4927 test st', '555-555-5555', true);

insert into customer (Email, Password, LastName, FirstName, Address, Phone, Router)
VALUES ('tester@test.com', 'password', 'Bobbyton', 'Bob', '3432 nonya ave', '208-123-4567', false);