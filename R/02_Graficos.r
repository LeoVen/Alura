# Importanto dataset duracao.csv

# Removendo tudo que está no IDE
rm(list=ls())

# Para limpar o console basta usar Ctrl + L

# Problema com pacote readr resolvido
remove.packages("readr")
install.packages('readr', repos='http://cran.us.r-project.org')

# Renomeando nome das colunas de um dataset
duracao <- rename(duracao, replace = c("user_id"="aluno", "course_id"="curso", "timeToFinish"="dias"))

# Criando um gráfico
plot(duracao$dias)

# Histograma
hist(duracao$dias)