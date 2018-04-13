# Importanto dataset duracao.csv

# install.packages("plyr")

# Removendo tudo que está no IDE
rm(list=ls())

# Para limpar o console basta usar Ctrl + L

# Problema com pacote readr resolvido
remove.packages("readr")
install.packages('readr', repos='http://cran.us.r-project.org')

# Renomeando nome das colunas de um dataset
# É preciso importar a biblioteca plyr
duracao <- rename(duracao, replace = c("user_id"="aluno", "course_id"="curso", "timeToFinish"="dias"))

# Criando um gráfico
plot(duracao$dias)

# Histograma
hist(duracao$dias)

# Definindo o numero de quebras em um histograma
hist(duracao$dias, breaks = 20)

# Incluindo título e labels
hist(duracao$dias, breaks = 20, main = "Histograma do Tempo", ylab = "Frequencia", xlab = "Tempo para conclusão")

# Limites dos eixos
hist(duracao$dias, breaks = 20, main = "Histograma do Tempo", ylab = "Frequencia", xlab = "Tempo para conclusão", ylim = c(0, 2500))

# Adicionando cores
hist(duracao$dias, breaks = 20, main = "Histograma do Tempo", ylab = "Frequencia", xlab = "Tempo para conclusão", ylim = c(0, 2500), col = "lawngreen")

# Arquivo png
png("histograma.png")
hist(duracao$dias, breaks = 20, main = "Histograma do Tempo", ylab = "Frequência", xlab = "Tempo para conclusão", ylim = c(0, 2500), col = "lawngreen")
dev.off()
