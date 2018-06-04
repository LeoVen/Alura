# Linux

## Processos

    ps - Listar processos
    kill - Matar processos
    killall - Matar todos os processos com um certo nome
    top - Consumo e Uso de RAM/CPU
    htop - Igual à top mas precisa ser baixado
    pstree - Árvore de processos

### Kill

    kill -signame -process_id
    kill -SIGKILL -2151

### Jobs

    jobs - Ver quais processos estão rodando
    fg - Rodar um processo no foreground
    bg - Rodar um processo no background

## Bash

    sh <script_file> - Roda um script

## locate

O linux tem um "banco de dados" que armazena onde todos os arquivos estão. O locate apenas faz a checagem desse "banco" e mostra onde arquivos com o nome passado por parêmetro está.

    locate <something>
    updatedb - Fazer o update do banco

### Which

O comando ```which``` diz onde está o arquivo que será executado se digitarmos um comando

    which <command_name>
    which cat

## Usuários

    su <username> - Trocar de usuário ou root
    sudo - Executar um comando como outro usuário ou o superuser
    adduser <user_name> - Adiciona um novo usuário

### chmod

Mudar as permissões de arquivos e pastas para usuários

    chmod <mod> <file/folder>

## Variáveis de Ambiente e PATH

Adicionando variáveis de ambiente para um único usuário

    PATH=$PATH:/desired/path/to/include

Note que a pasta ```/usr/bin``` é compartilhada com todos os usuários.

Para que esta variável de ambiente permanceça sempre que o usuário entrar no bash basta editarmos o arquivo ```.bashrc```. Sempre que um novo bash for iniciado esse script é rodado.

## wc

Usado para contar palavras, linhas, etc.

    wc <file_name>

Contagem de linhas em um arquivo

    cat <file_name> | wc -l

Contagem de Arquivos

    ls -l | wc -l

## apt

O apt é um package manager usado para baixar pacotes e programas.

    apt-get update - Usado para fazer update da lista de pacotes
    apt-get install <package_name> - Usado para instalar pacotes
    apt-get remove <package_name> - Usado para remover pacotes instalados
    apt list --installed - Listar pacotes instalados
    apt-cache search <something> - Usado para buscar algo na lista de pacotes

## dpkg

Usado para instalar programas que não estão listados. Na internet podemos baixar arquivos com a extensão ```.deb``` e usar o comando ```dpkg``` com a flag ```i``` para instalar o pacote.

    dpkg -i <file_name>.deb
    dpkg -r <package_name> - Remover o pacote instalado com dpkg

## Service

Usado para e reinicializar um serviço.

    /etc/init.d - Onde os serviços estão localizados
    service <service_name> start/stop/status - Comandos sobre serviços

## SSH

    apt-get install ssh
    ssh <user_name>@<ip_address> - Conectar remotamente
    scp <file_name> <user_name>@<ip_address>:/path/to/file - Enviar arquivos

Para copiar um arquivo de maneira recursiva usando ```scp``` é preciso usar a flag ```-r```.
