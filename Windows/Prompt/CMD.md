# Windows Prompt

>Os comandos não são case-sensitive

#### Write in prompt

	echo [message]

#### List directory

	dir

#### Change directory

	cd [dir_name]

#### Make directory

	mkdir [dir_name]

#### Remove directory

	rmdir [dir_name]

#### Move files from one folder to another

	move [file] [dir_name]

#### Display the contents of a text file

	type [file]

#### Display output, one screen at a time

	more [file]

#### Copies file_1 to new file_2

	copy [file_1] [file_2]

#### Delete file

	del [file]

#### Clear screen

	cls

#### Graphical display of folder structure

	tree

#### Current directory

	.

#### Parent directory

	..

#### Redirect command exit

	[command] > [file]

#### Concatenate command exit

	[command] >> [file]

#### Other commands

	echo %date%
	echo %time%

#### WMI Commands
	
	wmic

#### Batch

	@echo off

## set / setx

### set

>Set a PATH variable temporarily

	SET [variable=[character_string]]

### setx

>Set a PATH variable

	SETX [/S sistema [/U [domínio\]usuário [/P [senha]]]] var valor [/M]

# Programas usados

## cmder

#### Acessar configurações

	Windows + Alt + P

## RapidEE

>Editor de variáveis de ambiente. Deve ser iniciado como administrador.

* Criar novas variáveis
* Editar variáveis
* Adicionar novos valores
* Remover duplicatas e variáveis em branco
* Detectar caminhos inválidos

## Chocolatey

>Gerenciador de pacotes windows

#### Instalar pacote

	choco install [nome_pacote]

#### Desinstalar pacote

	choco uninstall [nome_pacote]

#### Listar pacotes que podem ser instalados pelo chocolatey

	choco list [nome_pacote]

#### Listar pacotes instalados no computador pelo chocolatey

	choco list -l

Observe que {choco list} é igual a {choco search}

## OneGet

>Gerenciador de pacotes nativo do Windows (Powershell e Windows 10 apenas)

