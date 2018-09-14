select a.nome, c.nome from aluno a join matricula m on m.aluno_id = a.id join curso c on m.curso_id = c.id;
select a.nome from aluno a where not exists (select m.id from matricula m where m.aluno_id = a.id);

select a.nome from aluno a 
where not exists (
	select m.id from matricula m
	where m.aluno_id = a.id and m.data < now() - interval 60 month
);

select * from aluno limit 0,2;
select * from aluno where email like '%dasilva.com' limit 0,2;

select c.nome as nome_curso, avg(n.nota) as nota_media from nota n 
join resposta r on r.id = n.resposta_id
join exercicio e on e.id = r.exercicio_id
join secao s on s.id = e.secao_id
join curso c on c.id = s.curso_id
group by c.nome;

select c.nome as nome_curso, count(m.id) as quantidade
from curso c
join matricula m on c.id = m.curso_id
group by c.nome;

select c.nome as nome_curso, avg(n.nota) as nota_media
from nota n
join resposta r on r.id = n.resposta_id
join exercicio e on e.id = r.exercicio_id
join secao s on s.id = e.secao_id
join curso c on c.id = s.curso_id
join aluno a on a.id = r.aluno_id
where a.nome like '%Santos%' or a.nome like '%Silva%'
group by c.nome;

select e.pergunta, count(r.id)
from exercicio e
join resposta r on e.id = r.exercicio_id
group by e.id;

select e.pergunta, count(r.id)
from exercicio e
join resposta r on e.id = r.exercicio_id
group by e.id
order by count(r.id) desc;

select
	a.nome as nome_aluno,
	c.nome as nome_curso,
	avg(n.nota) as nota_media
from nota n
join resposta r  on r.id = n.resposta_id
join exercicio e on e.id = r.exercicio_id
join secao s     on s.id = e.secao_id
join curso c     on c.id = s.curso_id
join aluno a     on a.id = r.aluno_id
group by c.nome, a.nome;


/* Nota: nao é possivel ter uma funcao de agrupamento junto com a funcao where.
 * Neste caso é preciso usar a funcao having. O having e usado para filtrar o 
 * resultado de um agrupamento.
 */
select
	a.nome as nome_aluno,
	c.nome as nome_curso,
	avg(n.nota) as nota_media
from nota n
join resposta r  on r.id = n.resposta_id
join exercicio e on e.id = r.exercicio_id
join secao s     on s.id = e.secao_id
join curso c     on c.id = s.curso_id
join aluno a     on a.id = r.aluno_id
group by c.nome, a.nome
having avg(n.nota) < 5;

select distinct tipo from matricula;

select c.nome, count(m.id) as matriculados from curso c join matricula m on m.curso_id = c.id group by c.nome;

select c.nome, count(m.id) as matriculados
from curso c
join matricula m on m.curso_id = c.id
where m.tipo in ('PAGA_PJ', 'PAGA_PF')
group by c.nome;

select e.pergunta, count(r.id)
from exercicio e
join resposta r on e.id = r.exercicio_id
join secao s on s.id = e.secao_id
join curso c on s.curso_id = c.id
where c.id in (1,3)
group by e.pergunta;

select
	a.nome as nome_aluno,
	avg(n1.nota) as nota_media,
	avg(n1.nota) - (select avg(n2.nota) from nota n2) as media_diff
from nota n1
join resposta r on r.id = n1.resposta_id
join exercicio e on e.id = r.exercicio_id
join secao s on s.id = e.secao_id
join curso c on c.id = s.curso_id
join aluno a on a.id = r.aluno_id
group by a.nome;

select
	a.nome as nome_aluno,
	avg(n1.nota) as nota_media,
	avg(n1.nota) - (select avg(n2.nota) from nota n2) as media_diff
from nota n1
join resposta r  on r.id = n1.resposta_id
join exercicio e on e.id = r.exercicio_id
join secao s     on s.id = e.secao_id
join curso c     on c.id = s.curso_id
join aluno a     on a.id = r.aluno_id
where a.id in (
	select m.aluno_id
	from matricula m
	where m.data > now() - interval 60 month)
group by a.nome;

select
	c.nome as nome_curso,
	count(m.id) as matriculas,
	count(m.id)/(select count(id) from matricula m) as media
from curso c
join matricula m on m.curso_id = c.id
group by c.nome;

select a.nome, r.resposta_dada from aluno a left join resposta r on r.aluno_id = a.id;

select a.nome, r.resposta_dada from aluno a left join resposta r on r.aluno_id = a.id and r.exercicio_id = 1;


