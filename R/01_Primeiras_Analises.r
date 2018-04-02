# Importando dataset aulas.xlsx

# Fazendo uma cópia de um dataset chamado aulas
attach(aulas)

# Opção da quantidade máxima que será exibida no console
options(max.print = 100000)

section_id

# Primeiros valores
head(section_id)

# Valores em ordem crescente
sort(section_id)

# Datasets são tratados como matrizes
# Aqui estamos pegando a linha 33137, coluna 3
aulas[33137,3] #999999

# Modificando o dado
aulas[33137,3] <- 3255

aulas[33137,3] #3255

# Porém 999999 continua pois a função attach apenas
# cria uma cópia do nosso banco de dados

sort(section_id)

# Mas o valor foi modificado nos dados originais

sort(aulas$section_id)

# Se mostramos o valor apartir do banco de dados ai sim
# temos o valor já modificado
aulas[33137,3]

# Pegando valores únicos
sort(unique(aulas$section_id))

# Tamanho de um resultado
# Neste caso a quantidade de section_id (videos) unicos
length(unique(aulas$section_id))

# Tabela com section_id unicos e a frequencia
table(aulas$section_id)

# Ordenado pela frequencia daquele dado
sort(table(aulas$section_id))

# Agora para outro dado (cursos)
sort(table(aulas$course_id))

# Quantidade de cursos unicos
length(unique(aulas$course_id)) #265

# Instalando biblioteca para usar novas funções
install.packages("plyr")

# Incluir uma biblioteca
library(plyr)

# Salvando saída da nova função de contagem
# Aqui é criado um novo objeto com a variável
# especificada em vars e a frequência de cada um
aux <- count(aulas, vars = "course_id")

# Salvar novo objeto
write.csv(aux, "popularidade.csv")
