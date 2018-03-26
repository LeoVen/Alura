# Conceitos de Estatística

## Tipos de Dados

### Ordinal

Quando temos uma ordem, mas não conseguimos medir precisamente a diferença de um para outro. Por exemplo quando avaliamos algo de 0 a 10, uma nota 5 pode ter significado diferente para cada pessoa, ou talvez um 8 não seja uma nota boa, etc.

### Intervalar

Igual à Ordinal porém a diferença entre um valor e outro é mensurável e precisa. Por exemplo temperatura.

### Racional

Pode ser mensurável e possuir uma ordem, mas, diferentemente, temos 0 que representa a ausência daquele dado.

### Categórico

Um dado é diferente do outro e não possuem relação, como categorias.

## Histograma

É um gráfico que tem, no eixo X, o __valor da variável sendo exibida__ (por exemplo, dinheiro, altura, temperatura, etc) e no eixo Y, __a frequência__ (ou seja, quantidade de vezes que aquele item aparece na distribuição).

## Média, mediana e moda

### Média

* Média aritmética
* Média aritmética ponderada
* Média geométrica
* Média harmônica
* Média quadrática

A média serve exatamente para o caso onde a distribuição é normal e não há muitos outliers na distribuição.

### Mediana

É a tendência central. Os valores são colocados em ordem crescente e tiramos o valor central.

### Moda

A Moda é aquele elemento que mais se repete na distribuição.

Tanto a mediana quanto a moda podem ser boas maneiras de descobrir a tendência a central. A média aritmética é facilmente afetada por outliers.

## Variabilidade, Dispersão de Dados, Outliers e Quartis

### Amplitude

É o maior valor menos o menor. Por exemplo, com o conjunto ```(3, 6, 7, 10, 11, 13, 30)``` temos que a amplitude é igual à ```30 - 3 = 27```.

### Outliers

São números extremos, geralmente muito grandes ou muito pequenos de uma distribuição ordenada, que podem ser eliminados na hora de analisar dos dados.

### Quartile

O primeiro quartil corresponde aos primeiros ```1/4``` dos dados ordenados, o segundo ```2/4```, e o terceiro quartil os ultimos ```1/4```. Esta técnica é boa em eliminar *outliers* e se chama __Distribuição por Quartis__. Uma forma de vizualização é o *Boxplot*.

## Variância e Desvio Padrão

### Variância

A variância é calculada por:

```( M₁² + M₂² + M₃² + ... + Mn² ) / n```

onde ```n``` é a quantidade de elementos e ```M₁, M₂, ..., Mn``` é dado por:

```Mn = (M - An)```

onde ```M``` é a média aritmética e ```An``` os números.

Assim temos que a variância é igual à média aritmética dos dados menos o número, tudo elevado ao quadrado, somados e dividido pela quantidade de elementos. Assim, a variância de n elementos é dada por:

	V(n) = [ (M - A₁)² + (M - A₂)² + (M - A₃)² + ... + (M - An)² ] / n

### Desvio Padrão

O desvio padrão é encontrado quando tiramo a raíz quadrada da variância:

	Dp = [V(n)]

Um desvio padrão próximo à 0 significa que os dados estão próximos à média.

## Amostra

Uma parte significativa e atingível da população, que usamos para nossos testes e estudos. Dado que a amostra apenas representa a população, e a população deve ter seus dados mais dispersos, subtrair 1 do divisor nos ajuda a aumentar a variância, e dessa forma ficar mais perto da variância da população. Quanto maior o tamanho da amostra, mais perto da variância da população o valor será. Esse menos 1 só é relevante para pequenas amostras.

## Degrees of Freedom

## Intervalos de Confiança

É o intervalo estimado de algum parâmetro estatístico. Ou seja, ao invés de afirmarmos que a média é "90", dizemos que a média está entre "88" e "92", com 95% de certeza. 95% é um número amplamente adotado como um intervalo de confiança. Não podemos usar 100% de confiança pois isso implicaria em termos um intervalo muito aberto, assim como 10% pois teríamos um intervalo muito fechado e provavelmente errado.

