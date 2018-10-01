explain select *, 
(select count(data_de_lancamento) from livros as l2 where l2.data_de_lancamento = l.data_de_lancamento)
as anteriores from livros l order by l.data_de_lancamento;

create index indice_por_lancamento on livros(data_de_lancamento);

show index from livros;

alter table livros drop index indice_por_lancamento;

create table books
(
	id integer primary key auto_increment not null,
	nome varchar(100) not null,
	data_de_lancamento date not null,
	index indice_por_lancamento (data_de_lancamento),
	autor_id integer not null
);

alter table usuarios change email_1 email_primario varchar(100);
alter table usuarios change email_2 email_secundario varchar(100);

alter table receitas drop column valor_total;