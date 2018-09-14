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
select * from compras where observacoes is null;

alter table compras modify observacoes varchar(255) not null;
alter table compras modify recebido tinyint(1) default '0';
alter table compras add column forma_pagamento enum('cartao', 'boleto', 'dinheiro');

update compras set forma_pagamento = 'dinheiro' where valor < 50;
update compras set forma_pagamento = 'boleto' where valor >= 50 and valor < 1000;
update compras set forma_pagamento = 'cartao' where valor >= 1000;

select sum(valor) from compras;
select forma_pagamento, sum(valor) as soma_total from compras group by forma_pagamento;
select forma_pagamento, count(valor) as total from compras group by forma_pagamento;
select recebido, sum(valor) as valor_total from compras group by recebido;

select month(data) as mes, year(data) as ano, sum(valor) as valor_total from compras group by month(data), year(data) order by year(data), month(data);
select month(data) as mes, year(data) as ano, avg(valor) as valor_total from compras group by month(data), year(data) order by year(data), month(data);


CREATE TABLE IF NOT EXISTS NOVAS_COMPRAS
(
	id int NOT NULL AUTO_INCREMENT,
	valor DECIMAL(10,2) NOT NULL,
	data DATETIME,
	observacoes TEXT,
	recebido TINYINT(1) DEFAULT 0,
	forma_pagamento ENUM('cartao', 'boleto', 'dinheiro') NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE COMPRADORES
(
	id INT NOT NULL AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL,
	endereco VARCHAR(100) NOT NULL,
	telefone VARCHAR(20) NOT NULL,
	PRIMARY KEY(id)
);