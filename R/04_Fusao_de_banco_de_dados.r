# Importanto dataset duracao.csv
# Importando dataset aulas.xlsx

# install.packages("plyr")

# Agregando e calculando a media de duracao de cada curso
sumario <- aggregate(duracao$dias, list(duracao$curso), mean, na.rm = T)

# Mudando o nome das colunas para usarmos o merge
sumario = rename(sumario, replace = c('Group.1'='curso', 'x'='dias'))
popularidade <- rename(popularidade, c('course_id'='curso', 'freq'='popularidade'))

# Popularidade e duração juntados por uma coluna 'curso' em comum
popularidade_duracao <- merge(sumario, popularidade, by = 'curso')
