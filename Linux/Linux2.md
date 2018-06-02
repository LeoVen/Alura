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