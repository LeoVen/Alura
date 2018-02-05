# Scrum

O Scrum é um framework ágil e sua principal característica é trabalhar com time-boxes: caixas de tempo cujo tamanho, uma vez definido, não muda durante a Sprint atual.

O Scrum tem uma forte metáfora com Rugby, onde todos os jogadores estão coordenando-se para sempre ter a posse da bola e ao final atingir o objetivo onde todos são considerados como um só. O time é visto como um só indivíduo.

## Team
* Product Owner
* Scrum Master
* Development Team

Todos os três fazem parte do time.

## Time-boxes e Sprints

### Time-boxes

Os time-boxes são caixas de tempo com capacidade definida, rígida e não negociável. Os sprints são a unidade básica dos time-boxes.

### Sprint

Sprint é a time-box básica do Scrum. Ela é o tempo que o time tem para agregar valor para o usuário do projeto.

### Duração de um Sprint

O tempo __limite para um sprint é de 1 mês__, mas seu tamanho pode variar de acordo com vários critérios.

No início de um projeto, quando os objetivos ainda não estão bem definidos ou o cliente ainda não se decidiu exatamente o que será desenvolvido no produto, os sprints tendem a ser menores porque ao final de cada um, após o review, é muito importante receber o máximo possível de feedbacks a partir do que foi feito para a execução das próximas tarefas.

Um sprint mais longo pode ser necessário quando precisamos digerir partes muito grandes do projeto. Assim, é preciso estender a duração do sprint. Outro ponto que pode acarretar no alargamento de um sprint é quando a equipe de desenvolvimento está desbravando novas tecnologias, precisando então de um certo tempo para que o time possa se familiarizar com a nova tecnologia após cada avanço.

Em sprints longos pode ser que o rendimento caia por falta de motivação. Por isso sprints mais curtos podem ser mais proveitosos, criando um ciclo mais rápido de feedback. Por outro lado, se diminuimos muito um sprint o estresse aumenta e isso pode ser maléfico para o desenvolvimento.

Achar a duração ideal de um sprint é muito importante. A duração da Sprint atual não pode ser alterada. No entanto, ao final de um ciclo, ela pode ser revista.

## Ciclo do Framework

>Planning > Development > Review Meeting > Retrospective

## *Review Meeting*

A *Review Meeting* é uma reunião na qual são mostrados os produtos elaborados durante o sprint. É a partir dela que recebemos feedbacks, e quanto mais retornos obtivermos, melhor será o rendimento do próximo sprint, evitando trabalhos desnecessários.

A Review é também um time-box e __não pode ultrapassar 2.5% do tempo da sprint__. Nela participam o time todo de desenvolvimento, o cliente e se possível também os usuários daquela aplicação. Esta é uma etapa muito importante do Scrum pois é nela onde os dois lados se entendem e se conhecem melhor.

### Como fazer a *Review Meeting*

#### Sugestão

#### 1. Fazer o usuário testar o produto

Ao fazermos o cliente testar o produto é possível que ele o utilize de maneira diferente daquilo que pensávamos. É útil para descobrir o que e como o usuário pensa.

Também podemos ver com mais clareza o que o cliente busca. As vezes atingimos exatamente o que ele buscava, mas as vezes acabamos criando algo totalmente diferente daquilo que o cliente queria, e é aqui onde ganhamos ótimos feedbacks para realizar mudanças no produto.

#### 2 Novas ideias... mas qual é a prioridade?

>*Product (Project) Backlog* é uma lista priorizada do que deve ser feito no projeto.

 Se recebemos novas idéias do cliente devemos ver onde ela se encaixa no Backlog. Qual a prioridade? É possível encaixá-la sem comprometer o custo e tempo? Será necessário mudar o escopo?

O Scrum troca de escopo com muita facilidade e frequência, e afirma que as variáveis de software não se fixam: custo, esforço, qualidade e tempo. Para Métodos Ágeis, a qualidade não pode ser sacrificada, e essa é uma regra que deveria ser levada bastante a sério.

>Mudar tempo e custo é bastante difícil, mas mudar escopo é mais simples.

#### Finalizando

No final perguntamos ao cliente se o sprint foi bem sucedido ou não e se atendeu as metas do *Planning* ou não.

### Definição de Pronto

A definição de pronto deve ser uma visão uniforme para o time todo. O critério de "Pronto" depende de cada equipe e deve preferívelmente ser estipulado já logo no início. Exemplo de critérios de Pronto:

1. Testes de aceitação automatizados;
2. Desenvolvimento utilizando testes de unidade e integração automatizados;
3. Code Review para garantir que o código está dentro do padrão que o time aceita;
4. Homologação, que é pedir para a pessoa que comentou sobre o incremento de tarefas fazer a verificação.

>O critério de pronto cresce conforme o tempo passa - Scrum Guide

## Retrospectiva

Entre a *Review Meeting* e a Retrospectiva não há tempo de desenvolvimento. Ela é o ultimo time-box do sprint. É a reunião mais importante de melhoria contínua. Ela precisa ser no máximo 5% do tempo do sprint e não durar mais que duas horas. Participam dela o Scrum Master, Product Owner e Desenvolvedores. Essa é a hora 

Para começar a retrospectiva, iniciamos citando o Prime Directive, inclusive vários facilitadores da comunidade ágil mundial iniciam assim. Prime Directive é a diretiva primária, que resume-se a um parágrafo com o seguinte conteúdo: não importa o que descobriremos nessa reunião, consideraremos que as pessoas agiram dessa forma devido aos conhecimentos que possuíam na época, tempo e recursos disponíveis. Considerando esses aspectos, as pessoas fizeram seu melhor, e agora devemos seguir adiante.

>"Regardless of what we discover, we understand and truly believe that everyone did the best job they could, given what they knew at the time, their skills and abilities, the resources available, and the situation at hand." -- Prime Directive by Norm Keith

### Como fazer a Retrospective

#### Sugestão

Uma maneira de começar com uma reunião de retrospectiva é cada um escrever em *post-its* pontos positivos e negativos do sprint, e em um quadro separado por Positivos e Negativos colá-los. Após essa primeira separação, fazemos uma agrupação das notas que mais se aproximam e assim é possível enxergar quais são as maiores dificuldades da equipe e quais pontos foram mais bem sucedidos. Após isso iremos levantar ações para combater esses pontos negativos e buscar sempre melhorar. Assim na próxima retrospectiva levantaremos quais ações foram feitas em relação à retrospectiva anterior e ficar numa constante melhora.

[Outras formas de fazer uma retrospectiva](http://www.funretrospectives.com/)

>A retrospectiva é a maior oportunidade, em cada Sprint, de promovermos melhorias no processo, no time e no andamento do projeto que está sendo desenvolvido.

## Daily Scrum

* O que fez?
* O que fará?
* Quais problemas enfrentados?

Participam Desenvolvedores, Scrum Master e Product Owner, com duração máxima de 15 minutos.

### Quando fazer a Daily Scrum

* Sempre no mesmo horário
* Sempre no mesmo lugar

O lugar fica a critério da empresa. Já o horário (como uma sugestão) é preferível evitar os extremos do dia pois pode ser que alguns membros acabam saindo antes ou entrando mais cedo, tendo que tornar esse horário mais flexível.

## Planning Meeting

Participam Desenvolvedores, Scrum Master e Product Owner.

Esse é o momento em que se inicia a Sprint. A Planning Meeting limita-se a 5% da Sprint, e é um processo de planejamento. O time se reúne com o Scrum Master, que trabalha mais a parte da facilitação, os desenvolvedores, para pensarem na parte mais técnica de como realizar certas tarefas. Nisso, o Product Owner é responsável por priorizar um grupo de itens que agregue o máximo de valor possível.

### Como implementar

O P.O. chega na reunião com o Product Backlog, lista ordenada ou priorizada dos itens a serem feitos durante o projeto. A ideia é sair da reunião com a lista priorizada dos itens e sub-itens técnicos que o time está comprometido a fazer durante a Sprint em questão (o Sprint Backlog).

Uma vez que o Sprint Backlog foi decidido, o time olha para as histórias selecionadas e cria uma meta: uma frase que exprime o maior valor que esse Sprint vai trazer para o usuário!

### Resumidamente

* Enquanto não passar um pouco do que o time consegue fazer na Sprint:
 * P.O. explicando o item de maior prioridade da visão de negócios;
 * Desenvolvedores tiram dúvidas de entendimento e o discutem tecnicamente;
 * Desenvolvedores atribuem uma estimativa de esforço à história.
* Desenvolvedores e P.O. negociam o Sprint Backlog
* Time todo monta uma meta para a Sprint

## Product Backlog e Sprint Backlog

Cada item do Backlog deve ser algo que agregue valor ao usuário, seja lá em que formato.

### Sugestão: aplicar o *Story*

A história é um item que agrega valor ao usuário, escrita de forma bem diferente ao caso de uso, deve ter um título, um porquê e para quem esse item é importante. O template da história pode ser feito com um cartão de papel. Ela serve para convidar o desenvolvedor a tirar dúvidas sobre os detalhes de uma tarefa. A ideia é que ela seja legível e fluente.

#### Tasks

Tarefas são subitens de uma história, mais focados na parte técnica. Eles servem para conseguirmos trabalhar paralelamente sobre uma história e, assim, aumentar a velocidade de produção de valor para o usuário.

Exemplo:

* __para__: "motivar meu time a bater a meta de vendas"
* __como__: "Camila, gerente comercial"
* __quero__: "que toque uma musica quando atingir a meta de vendas do dia"

Outro exemplo fora do ambiente de trabalho:

__Sala de Estar__

* __Para...__ receber meus amigos para degustar queijos e vinhos com conforto
* __Eu, como...__ morador
* __Quero...__ uma sala de estar de 20m², com carpete de madeira, grandes almofadas soltas pelo chão, uma mesinha central retrátil, uma mini adega para 6 vinhos e sistema de som ambiente.

### Product Backlog

O artefato padrão no Scrum é o Product Backlog, uma lista ordenada, que prioriza todos os itens de negócio e histórias até o final do projeto. Quem cuida dessa lista é quem tem o domínio sobre o que entra e sai, e essa pessoa, o *Product Owner*, também estabelece prioridades nessa lista.

Se algo perde importância no Backlog o item acaba ficando para baixo na lista de prioridade, e isso vai sendo deixado de lado até que o projeto acabe. Se ainda for interessante realizar itens e tarefas que ficaram para fora do prazo estimado, pode ser feito um adendo de contrato, prosseguindo-se a execução desses itens caso agregarem valor suficiente.

#### Grooming

O processo de quebrar histórias muito grandes em menores de maneira que cada uma siga agregando valor ao usuário final é chamada de *Grooming* do *Product Backlog*.

### Sprint Backlog

O Sprint Backlog, diferentemente, é do time como um todo, e a regra é que a equipe pode renegociar prioridades (lembrando que o time é composto de desenvolvedores, P.O. e Scrum Master). Assim, é possível mudar o escopo de maneira a agregar valor - essa é uma decisão interna do time.

O Sprint Backlog possui a regra de que o cliente não pode dar sua opinião. Se algo entrou para ser feito nessa Sprint, então é porque são itens de maior prioridade. Se o cliente pensa em mexer nisso é porque o P.O. não conversou direito com ele, ou as prioridades não estão bem estabelecidas, e ele muda de opinião o tempo inteiro.

### Quem altera os Backlogs

* *Product Backlog*: apenas o P.O. altera, mas todos podem influenciá-lo, tanto desenvolvedores, scrum master e clientes.
* *Sprint Backlog*: o cliente não pode alterá-lo ou influenciá-lo. Apenas o time altera esse backlog, renegociando internamente o escopo quando necessário, quebrando melhor as histórias em tarefas, etc.

### Cancelar Sprint

A única razão pela qual se faz um cancelamento de Sprint no Scrum é quando o Sprint Backlog se altera tanto a ponto da meta não fazer mais sentido. Os cancelamentos também podem ocorrer no caso de problema de comunicação grave, um cliente muito indeciso ou eventualmente outro tipo de razão externa, como uma justificativa legal. No entanto tais situações não são comuns ou não devem ser recorrentes.

### Resumidamente

* O *Product Backlog* é a lista priorizada das histórias que agregam valor para o cliente. São histórias que envolvem o projeto inteiro. Somente o P.O. mexe nele, mas todo o time pode palpitar.

* O *Sprint Backlog* engloba histórias e tarefas que estão no topo das prioridades. Conforme os itens entram nele, já quebramos as histórias em tarefas. No Sprint Backlog o time altera essas tarefas sem que o cliente palpite sobre elas.

Enquanto o *Product Backlog* foca no que agrega valor para o usuário (histórias), o *Sprint Backlog* acrescenta a isso as subdivisões técnicas das histórias (tarefas), já que ele já foca no planejamento para execução das histórias.

## Scrum Master

