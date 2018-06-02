# Linux

## Manipulação de Arquivos e Pastas

```
mkdir -> Make Directory
rmdir -> Remove Directory
rm    -> Remove
cp    -> Copy
mv    -> Move
touch -> Change date
```
### ZIP

    zip -r <zip_name.zip> <directory>
    unzip <zip_name.zip>

### TAR

    tar -cz <directory>
    tar -x < file.tar.gz

Nota: as flags ```c``` e ```z``` significam ```create``` e ```zip``` respectivamente. A flag ```x``` significa e__x__tract

### Date

    date "+%d/%m/%Y %H:%M:%S"

### Head - Tail

Mostra as primeiras 10 linhas do documento

    head <file_name>

Mostra as ultimas 10 linhas do documento

    tail <file_name>

É possível passar a flag ```-n``` para definir quantas linhas serão vistas

### Less

    less <file_name>

### Vi - Vim

Editores de Texto pelo terminal

    vi <file_name>
    vim <file_name>

