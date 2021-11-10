create database  Processo_seletivo
default charset utf8
default collate utf8_general_ci;

create table cep(
	cep varchar(9) not null unique,
    logradouro varchar(90),
    bairro varchar(20),
    localidade varchar(20) not null,
    uf varchar(2) not null
)default charset utf8;

select * from cep;