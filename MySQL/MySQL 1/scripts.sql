CREATE TABLE IF NOT EXISTS COMPRAS
(
	id int NOT NULL AUTO_INCREMENT,
	valor decimal(10,2),
	data datetime,
	observacoes text,
	recebido tinyint(1),
	PRIMARY KEY (id)
);

insert into compras (valor, data, recebido, obs) values (1500.0, '2014-05-14', 1, 'Geladeira nova porque a velha quebrou');
insert into compras (valor, data, recebido, obs) values (100.0, '2007-05-12', 'COMPRAS DE MAIO', 1);


select * from compras where valor between 200 and 700;
select * from compras where data between '2010-01-01' and '2010-04-01';
