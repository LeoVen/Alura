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

## Intervalos de Confiança

```R
> lizard = c(6.2,6.6,7.1,7.4,7.6,7.9,8,8.3,8.4,8.5,8.6,8.8,8.8,9.1,9.2,9.4,9.7,9.9,10.2,10,11.3,11.9)
> # Teste que mostra o intervalo de confiança
> t.test(lizard)

        One Sample t-test

data:  lizard
t = 29.169, df = 21, p-value < 2.2e-16
alternative hypothesis: true mean is not equal to 0
95 percent confidence interval:
 8.143041 9.393323
sample estimates:
mean of x 
 8.768182 

> # Com conf.level podemos adotar um intervalo de confiança
> t.test(lizard, conf.level=0.7) # 70%

        One Sample t-test

data:  lizard
t = 29.169, df = 21, p-value < 2.2e-16
alternative hypothesis: true mean is not equal to 0
70 percent confidence interval:
 8.448739 9.087625
sample estimates:
mean of x 
 8.768182 

```

## Testes

### Gerar dados em um dado intervalo

```R
> # Gerar n dados em um intervalo de x1 a x2
> inter <- runif(n, x1, x2)
# Agora temos uma lista de n valores que vão de x1 a x2
```

### Student t-Test

```R
> # Compara duas amostras normais
> null <- runif(100, 37.9, 38.8)
> hip <- runif(100, 36.0, 38.2)
> t.test(null, hip)

        Welch Two Sample t-test

data:  null and hip
t = 19.693, df = 128.17, p-value < 2.2e-16
alternative hypothesis: true difference in means is not equal to 0
95 percent confidence interval:
 1.193505 1.460128
sample estimates:
mean of x mean of y 
 38.38168  37.05486 

```

### Wilcoxon Test

```R
> # Compara duas amostras não necessariamente normais
> null <- runif(100, 37.9, 38.8)
> hip <- runif(100, 36.0, 38.2)
> wilcox.test(null, hip)

        Wilcoxon rank sum test with continuity correction

data:  null and hip
W = 9861, p-value < 2.2e-16
alternative hypothesis: true location shift is not equal to 0

```

## Correlação

```R
> # Correlação entre dois dados
> d1 <- c(1, 2, 3, 4)
> d2 <- c(2, 4, 6, 8)
> cor(d1, d2)
[1] 1
> d2 <- c(8, 6, 4, 2)
> cor(d1, d2)
[1] -1
> # É possível definir explicitamente o método
> d2 <- c(22, 28, 43, 26)
> cor(d1, d2, method="pearson")
[1] 0.3797547
> cor(d1, d2, method="spearman")
[1] 0.4
```

## Linear Regression

```R
> # Regressão Linear usando lm (Linear Model)
> d1 <- c(37, 40, 78, 45)
> d2 <- c(22, 28, 43, 26)
> lm(formula = d1 ~ d2)

Call:
lm(formula = d1 ~ d2)

Coefficients:
(Intercept)           d2  
     -9.794        2.010  

> # Assim temos que a função é dada por
> # f(x) = -9.794 + 2.01 * x
> # É possível usar apenas
> lm(d1 ~ d2)
# Resultado
```

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

### Desenhar Linhas

```R
> lizard = c(6.2,6.6,7.1,7.4,7.6,7.9,8,8.3,8.4,8.5,8.6,8.8,8.8,9.1,9.2,9.4,9.7,9.9,10.2,10,11.3,11.9)
> mean <- mean(lizard)
> median <- median(lizard)
> t.test(lizard)

        One Sample t-test

data:  lizard
t = 29.169, df = 21, p-value < 2.2e-16
alternative hypothesis: true mean is not equal to 0
95 percent confidence interval:
 8.143041 9.393323
sample estimates:
mean of x 
 8.768182 

> hist(lizard)
> abline(v=mean, col="red", lwd=2)
> abline(v=median, col="blue", lwd=2)
> abline(v=9.393323, col="green", lwd=2)
> abline(v=8.143041, col="green", lwd=2)
# Mostra histograma com linhas traçadas onde:
# Verde: Intervalo de Confiança
# Vermelho: média aritmética
# Azul: mediana
```

>Ver hist.png