# R


## Básico

```R
> # Operador de atribuição
> list <- 2
> # Agrupar variáveis em forma de lista ou vetor
> list <- c(1, 2, 3, 3, 4, 4, 4, 6, 7, 7)
> # Criar um histograma com a lista
> hist(list)
> # Para ver a documentação
> ?function
```

## Média, Mediana e Moda

### Média

```R
> # Média mean()
> list <- c(1, 1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 7)
> mean(list)
[1] 4
```

### Mediana

```R
> # Mediana median()
> list <- c(1, 1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 7)
> median(list)
[1] 3.5
```

### Moda

```R
> # Criar função que calcula a moda:
> Mode <- function(x) {
+      ux <- unique(x)
+      ux[which.max(tabulate(match(x, ux)))]
+ }
> # Usando a função
> Mode(list)
[1] 3
```

## Variância e Desvio Padrão

### Variância

```R
> list1 <- c(1, 1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 7)
> # Função que calcula a variância (Variance)
> var(list1)
[1] 4.727273
```

### Desvio Padrão

```R
> list1 <- c(1, 1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 7)
> # Função que calcula o desvio padrão (Standard Deviation)
> sd(list1)
[1] 2.174229
```

## Ler dados de um arquivo

### CSV

```R
> # Importar dados de um arquivo .csv
> data <- read.csv(file="C:/Users/myUser/Documents/data.csv")
> # Agora a variável data é um dataset
> # Para acessarmos uma coluna de um dataset usamos o $
> data$X1
 [1] 1 2 3 3 3 4 5 6 6 7 7
```

>Ver data.csv

## Outros

### Boxplot

```R
> list <- c(1, 1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 7)
> boxplot(list)
# É gerado um gráfico do tipo boxplot. É possível passar mais de uma lista
> # Boxplot com vários dados
> list1 <- c(1, 1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 7)
> list2 <- c(1, 1, 1, 3, 3, 4, 5, 6, 6, 6, 6, 8)
> list3 <- c(2, 2, 2, 2, 3, 3, 5, 6, 6, 7, 7, 7)
> list4 <- c(1, 2, 3, 3, 4, 4, 5, 6, 6, 6, 8, 8)
> list5 <- c(1, 1, 2, 2, 3, 4, 5, 6, 7, 7, 8, 9)
> boxplot(list1, list2, list3, list4, list5)
# Gráfico com boxplot de todas as listas
> # É possível também salvá-lo como uma imagem
> png(file="/Users/myUser/documents/boxplot.png", width=700, height=700)
> boxplot(list1, list2, list3, list4, list5)
> dev.off() # Para enviar o buffer para o arquivo de imagem previamente configurado.
```

>Ver boxplot.png

### Sumário do conjunto

```R
> summary(list)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
   1.00    2.75    3.50    4.00    6.00    7.00 
```

### Testando se dados são normais ou não

```R
> # Normality test
> shapiro.test(list)

        Shapiro-Wilk normality test

data:  num
W = 0.91823, p-value = 0.2716
```

Se ```p-value``` for menor que ```0.05``` a distribuição não é normal.

```R
```