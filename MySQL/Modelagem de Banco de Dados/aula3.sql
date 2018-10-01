create table medicos (
	id integer primary key auto_increment not null,
	crm varchar(50) not null,
	nome varchar(100) not null
);

create table receitas (
	id integer primary key auto_increment not null,
	medico_id int not null,
	nome_remedio varchar(100) not null,
	valor decimal(10,2) not null,
	quantidade int not null,
	valor_total decimal(10,2),
	FOREIGN KEY (medico_id) REFERENCES medicos(id)
);

INSERT INTO medicos(crm, nome) values ('889999-PR', 'Lucas da Silva');
INSERT INTO medicos(crm, nome) values ('987654-SP', 'Maria dos Santos');
INSERT INTO medicos(crm, nome) values ('997755-RJ', 'Ivá Souza');
INSERT INTO medicos(crm, nome) values ('118745-DF', 'Paula Barbosa');
INSERT INTO medicos(crm, nome) values ('765930-CE', 'Celina Prates');

INSERT INTO receitas(medico_id, nome_remedio, valor, quantidade, valor_total) values (1, 'Pura t4', 30.50, 2, 61.0);
INSERT INTO receitas(medico_id, nome_remedio, valor, quantidade, valor_total) values (2, 'Gadernal', 6.30, 4, 25.20);
INSERT INTO receitas(medico_id, nome_remedio, valor, quantidade, valor_total) values (3, 'Sildenafila', 68.10, 10, 681.00);
INSERT INTO receitas(medico_id, nome_remedio, valor, quantidade, valor_total) values (4, 'Vasopril', 80.70, 5, 403.50);
INSERT INTO receitas(medico_id, nome_remedio, valor, quantidade, valor_total) values (5, 'Allegra', 46.70, 1, 46.70);