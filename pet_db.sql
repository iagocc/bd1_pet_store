create table pet_owner (
	id int auto_increment primary key,
    cpf char(11) unique,
    owner_name varchar(64),
    contact varchar(64)
);

create table pet (
	id int auto_increment primary key,
    pet_name varchar(64),
    type varchar(64),
    breed varchar(64),
    owner_id int,
    foreign key(owner_id) references pet_owner(id)
);