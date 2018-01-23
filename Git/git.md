>* Doctype        : Info
* Created by      : Leonardo Vencovsky
* Together with   : niemand / ninguém / nadie / nobody ~~~~~~
* Date            : 21/01/2018
* Last modified   : 23/01/2018
* Editor          : Sublime Text 3
* Inspiration     : Alura [www.alura.com.br]  Git: Controle e compartilhe seu código
* Language        : Portuguese
* Anotações sobre Git

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

## O Ciclo básico do Git

### Criando um repositório

	mkdir NomeRepositório

Para criar uma pasta com o nome "NomeRepositório". Em seguida precisamos inicializar essa nova pasta como um repositório Git:

	cd NomeRepositório
	git init

## Mais comandos

Para listar todos os arquivos dentro de cada pasta:

	git ls-files

Para ver o status do nosso repositório:

	git status

