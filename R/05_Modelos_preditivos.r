# Usando as funções usadas em 04_Fusao_de_banco_de_dados.r

install.packages("ggplot2")

library(ggplot2)

# Criando o gráfico
grafico <- ggplot(popularidade_duracao, aes(dias, popularidade))

# Adicionando os pontos
grafico <- grafico + geom_point()

# Adicionando a curva
grafico <- grafico + geom_smooth()

# Mostrando o gráfico
grafico