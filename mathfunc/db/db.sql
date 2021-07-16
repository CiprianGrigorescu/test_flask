create table requests
(
	id integer not null
		constraint requests_pk
			primary key autoincrement,
	request_verb varchar(10) not null,
	request_method varchar(30) not null,
	request_params text not null,
	added datetime not null
);

create unique index requests_id_uindex
	on requests (id);
