# Importanto dataset duracao.csv

# install.packages("plyr")

# install.packages("plyr")

# Removendo campos nulos (not available) = True
mean(duracao$dias, na.rm = T)

median(duracao$dias, na.rm = T)

# Sumário estatístico
summary(duracao$dias)
# Ou
summary(duracao)

# Numero de linhas
dim(duracao)[2]

# Numero de colunas
dim(duracao)[2]

# Quantidade de cursos unicos
length(unique(duracao$curso))

# Quantidade de alunos unicos
length(unique(duracao$aluno))


