# Redes

Uma rede de computadores é formada por um conjunto de máquinas eletrônicas com processadores capazes de trocar informações e partilhar recursos.

### ping

	ping

Dentro da ferramenta administrativa do ping temos o protocolo ICMP, sendo ele o responsável por mandar uma requisição (Echo Request) para máquina remota e esperar um retorno dessa máquina remota (Echo Reply).

### TTL

O TTL seria uma informação dentro do pacote do IP que informa qual é a máxima quantidade de hops que minha informação pode passar antes de ser descartada. É a quantidade de máquinas que ela vai poder passar no caminho.

### Traceroute

	tracert

A principal funcionalidade do traceroute é verificar a rota que a minha informação levou para chegar até a máquina de destino. Isso porque, em redes de computadores temos o que chamamos de rede não determinística, ou seja, não necessariamente um pacote de informação vai ser transferido pela mesma rota do anterior com o mesmo intervalo de tempo. Isto se deve a muitos fatores, por exemplo, uma máquina que pode estar congestionada ou um problema no link de comunicação, etc.

Quando nós temos uma máquina que retornou (\*) e passou a informação para uma próxima máquina, isso provavelmente indica que o administrador dessa máquina desabilitou a resposta ao nosso chamado. O que acontece seria que esse tipo de teste pode ser interpretado como uma tentativa de “scanear” possíveis portas abertas e vulnerabilidades que possam existir, caso seja usado por um usuário malicioso, pode ser usada como uma forma de reconhecimento da rede dessa possível vítima para que assim possa explorar possíveis falhas.

### Nslookup

	nslookup

O Nslookup pode ser usado para descobrirmos o endereço IP de um domínio, bem como saber detalhes mais avançados de DNS, para saber se nosso serviço está sendo direcionado para a máquina de destino, por exemplo.

### Hub

O Hub é um equipamento utilizado para interconectar diversos dispositivos finais.

### NAT

NAT é um método de tradução de endereços privados e públicos.

### Servidor

Servidor é uma máquina centralizada que oferece serviços a um cliente (ex: computador)

### Máscara de rede

Máscara de rede é usado para determinar se dois equipamentos estão na mesma rede

### Tipos de Cabos

Caso tenhamos o mesmo padrão de cores na duas pontas do cabo, chamamos de cabo direto, pois as mesmas cores estão nas mesmas posições nas duas pontas.

Caso tenhamos um padrão de cores diferente em cada ponta do cabo, teremos o que chamamos de cabo cruzado.

Algumas placas de rede mais modernas possuem o padrão auto-MDIX, dessa forma, se as duas placas de rede estiverem configuradas, elas poderão corrigir essa questão da polaridade e se comunicarem

### Roteador

A função do roteador é interconectar redes encaminhando seus pacotes de dados, os Switches e hubs são usados somente para conexão na minha rede local.

## Classes de Redes

| Classe | Intervalo |    Máscara    |
|:------:|:---------:|:-------------:|
|    A   |  1 - 126  |   255.0.0.0   |
|    B   | 128 - 191 |  255.255.0.0  |
|    C   | 192 - 223 | 255.255.255.0 |
|    D   | 224 - 239 |       -       |
|    E   | 240 - 255 |       -       |

As classes A, B e C são usadas para máquinas. Já a classe D é reservada para multicasting e a classe E é reservada para experimentos.

O IP 127.0.0.1 é uma faixa de IP reservada para a rede interna da placa de rede para testes e validar operamento.

### IP privado

Dentro de cada classe de IP temos uma faixa de IP privados onde não será possível comunicar-se com a internet, apenas na rede local.

| Classe |    Intervalo Privado    |
|:------:|:-----------------------:|
|    A   |         10.X.X.X        |
|    B   | 172.16.X.X - 172.31.X.X |
|    C   |       192.168.X.X       |

## Endereços Reservados

### Endereços Reservados da Classe A

Uma Rede da classe A com endereço IP ```K.X.Y.Z``` :

	Máscara de Rede : 255.0.0.0
	Reservado para o endereço da rede : K.0.0.0
	Reservado para broadcast : K.255.255.255

### Endereços Reservados da Classe B

Uma Rede da classe B com endereço IP ```K.X.Y.Z``` :

	Máscara de Rede : 255.255.0.0
	Reservado para o endereço de rede : K.X.0.0
	Reservado para broadcast : K.X.255.255

### Endereços Reservados da Classe C

Uma Rede da classe B com endereço IP ```K.X.Y.Z``` :

	Máscara de Rede : 255.255.255.0
	Reservado para o endereço de rede : K.X.Y.0
	Reservado para broadcast : K.X.Y.255

## DHCP

Os servidores DHCP (Dynamic Host Configuration Protocol) alocam dinamicamente endereços IPs a clientes (máquinas).

Quando um endereço IP é atribuído a uma máquina, dizemos que a configuração foi dinamicamente alocado. Os servidores DHCP normalmente possuem o que chamamos de “lease time”, ou seja possui um tempo de alocação de um endereço IP a uma máquina, quando esse tempo é expirado é preciso ocorrer uma renovação de endereço IP.
