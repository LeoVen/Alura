# Git

>Sistemas de versionamento que atuam em servidores

### Alguns sistemas de controle de versão:
- CVS (Concurrent Versions System)
- SVN (Apache Subversion)

### O git é um sistema de controle de versões da segunda geração
- Controle de versão distribuído
- Offline

## GitHub

O GitHub é uma plataforma online com controle de versão do git. Para usar o GitHub é preciso baixar primeiro o Git.

Para __clonar__ um projeto usamos, no prompt de comando:

	git clone htpps://github.com/user/project_name.git

Observe que é preciso adicionar ".git" no final da URL

## Comandos Básicos

### Tags

São os textos que usamos para controlar as versões. Como por exemplo "v0.1" ou "v.1.0.12" ou também "v1.x.3"

#### tag
Para vizualizar as Tags, escrevemos no prompt de comando:

	git tag

#### checkout

Este comando é usado para trocar a versão de um repositório. Como por exemplo, trocar para a versão "v1.2":

	git checkout v1.2

É também usado para fazer branches.

#### diff

E como saber o que mudou nos arquivos em cada versão? Com o comando diff podemos ver isso entre arquivos ou diretórios.

	git diff v0.1 v0.2

#### blame

Usamos o blame para consultar quem foi o autor que modificou certa linha

	git blame index.html

#### status

Para ver o status do nosso repositório e seus arquivos:

	git status

#### ls-files

Para listar todos os arquivos dentro de cada pasta:

	git ls-files

## git add + git commit

### Configurando usuário

Para configurarmos o usuário e e-mail:

	git config --global user.name "Your Name"
	git config --global user.mail "you@example.com"

Usa-se --global se queremos configurar para o computador todo. Se o omitimos, faremos as configurações apenas para o atual repositório.

### Criando um repositório

	mkdir NomeRepositório

Para criar uma pasta com o nome "NomeRepositório". Em seguida precisamos inicializar essa nova pasta como um repositório Git:

	cd NomeRepositório
	git init

#### add

Para adicionar arquivos ao rastreamento e que este entre na Stagin Area na hora de atualizar o repositório:

	git add arquivo.html

Ver também:

	git add -i

#### commit

Para atualizarmos o repositório com os novos arquivos e/ou modificados (adicionados pelo add) devemos usar o git commit:

	git commit -m "Uma menssagem aqui"

Note que a flag -m significa que o que vem a seguir será uma menssagem que irá descrever as alterações

## O ciclo básico

Existem 3 seções de um Git:

* Working Tree (Working Directory)
* Staging Area (Index)
* .git Directory (Repository) (HEAD)

>Ver imagem

### Working Directory

O *Working Directory* pode estar "*clean*" quando não há diferença entre os arquivos armazenados no repositório e os arquivos atualmente no repositório sendo trabalhado. Ou pode estar 