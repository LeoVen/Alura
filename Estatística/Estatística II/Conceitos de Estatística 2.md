# Conceitos de Estatística II

## Provando ou Desprovando

### Testes de Hipótese

A Hipótese Nula ```H0``` é a hipótese que buscamos anular; já a Hipótese Alternativa ```Halt```, que é o que buscamos provar, é uma hipótese logicamente contrária à Hipótese Nula, ou seja, se ```H0``` é falso, logo ```Halt``` é verdadeiro e vice-versa.

### p-value

O p-value representa a probabilidade daquela amostra ter acontecido dentro da população. Se a chance é pequena, ou seja um evento muito raro aconteceu, então optamos por descartar a hipótese nula, e dizer que ela pode não ser verdade.

Se o p-value for menor que ```0.05```, podemos descartar ```H0```. Maior que isso caimos no caso onde temos uma fraca evidência contra a hipótese nula.

### Tests

* One-sided test
* Two tailed test

### Resumidamente

* Verificamos se uma hipótese é verdadeira ou não negando uma hipótese, a Hipótese Nula e assumindo que a outra é verdadeira, a Hipótese Alternativa;
* Escolhemos um teste - dentre vários possíveis;
* Por probabilidade calculamos a chance da mudança acontecer na distribuição anterior;
* Se a chance for baixa, ou seja o *p-value*, descarto ```H0```, logo ```Halt``` é verdadeiro.

## Correlação e Causalidade

### Correlação

Correlação indica a força do relacionamento entre duas variáveis. Se há correlação, isso quer dizer que quando uma é alterada, a também é alterada junto. Uma correlação de 0.9 indica uma forte correlação positiva entre as duas variáveis. Já uma correlação de 0.2 indica uma fraca correlação positiva entre as duas variáveis. E por fim, uma correlação de -0.9 indica uma forte correlação negativa entra as duas variáveis, ou seja, enquanto uma cresce, a outra aumenta. Assim temos que a correlação ```C``` pode variar entre ```-1 ≤ C ≤ 1``` . Uma correlação de 0 significa que não há correlação entre as variáveis.

### Causalidade

Não é porque duas variáveis são correlacionadas, que isso implica necessariamente em uma ser a causa da outra. Pode até haver uma correlação, mas não quer dizer que uma implica na outra. Podem haver diversas coincidências.

### Teste de Pearson

Testes para distribuições normais.

### Teste de Spearman

Testes para distribuições não normais.

## Regressão Linear

Regressão Linear é uma equação para se estimar a condicional (valor esperado) de uma variável y, dados os valores de algumas outras variáveis x. Usamos regressão linear para entender como duas variáveis funcionam, e tentar prever possíveis números que não estão dentro da distribuição atual. A ideia por trás da regressão linear é encontrar a melhor função de primeiro grau, que explica a distribuição dos dados.

O problema é que às vezes uma simples função de primeiro grau pode não ser suficiente. É por isso que antes de aplicá-la, é preciso olhar a distribuição e ver o quanto a função realmente se aproxima dos pontos já conhecidos.