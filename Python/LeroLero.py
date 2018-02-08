from random import *

def main():

    print("Quantas frases você gostaria de formar?")
    j = int(input())

    for i in range(j):
        n = randint(1, 3)
        if n == 1:
            f1()
        elif n == 2:
            f2()
        elif n == 3:
            f3()

def f1():

    r = [ ["Caros amigos, ", "Por outro lado, ", "Assim mesmo, ", "No entanto, não podemos esquecer que ", "Do mesmo modo, ", "A prática cotidiana prova que ", "Nunca é demais lembrar o peso e o significado destes problemas, uma vez que ", "As experiências acumuladas demonstram que ", "Acima de tudo, é fundamental ressaltar que ", "O incentivo ao avanço tecnológico, assim como ", "Não obstante, ", "Todas estas questões, devidamente ponderadas, levantam dúvidas sobre se ", "Pensando mais a longo prazo, ", "O que temos que ter sempre em mente é que ", "Ainda assim, existem dúvidas a respeito de como ", "Gostaria de enfatizar que ", "Todavia, ", "A nível organizacional, ", "O empenho em analisar ", "Percebemos, cada vez mais, que ", "No mundo atual, ", "É importante questionar o quanto ", "Neste sentido, ", "Evidentemente, ", "Por conseguinte, ", "É claro que ", "Podemos já vislumbrar o modo pelo qual ", "Desta maneira, ", "O cuidado em identificar pontos críticos n", "A certificação de metodologias que nos auxiliam a lidar com "],
        ["a execução dos pontos do programa ", "a complexidade dos estudos efetuados ", "a contínua expansão de nossa atividade ", "a estrutura atual da organização ", "o novo modelo estrutural aqui preconizado ", "o desenvolvimento contínuo de distintas formas de atuação ", "a constante divulgação das informações ", "a consolidação das estruturas ", "a consulta aos diversos militantes ", "o início da atividade geral de formação de atitudes ", "o desafiador cenário globalizado ", "a mobilidade dos capitais internacionais ", "o fenômeno da Internet ", "a hegemonia do ambiente político ", "a expansão dos mercados mundiais ", "o aumento do diálogo entre os diferentes setores produtivos ", "a crescente influência da mídia ", "a necessidade de renovação processual ", "a competitividade nas transações comerciais ", "o surgimento do comércio virtual ", "a revolução dos costumes ", "o acompanhamento das preferências de consumo ", "o comprometimento entre as equipes ", "a determinação clara de objetivos ", "a adoção de políticas descentralizadoras ", "a valorização de fatores subjetivos ", "a percepção das dificuldades ", "o entendimento das metas propostas ", "o consenso sobre a necessidade de qualificação ", "o julgamento imparcial das eventualidades "],
        ["nos obriga à análise ", "cumpre um papel essencial na formulação ", "exige a precisão e a definição ", "auxilia a preparação e a composição ", "garante a contribuição de um grupo importante na determinação ", "assume importantes posições no estabelecimento ", "facilita a criação ", "obstaculiza a apreciação da importância ", "oferece uma interessante oportunidade para verificação ", "acarreta um processo de reformulação e modernização ", "pode nos levar a considerar a reestruturação ", "representa uma abertura para a melhoria ", "ainda não demonstrou convincentemente que vai participar na mudança ", "talvez venha a ressaltar a relatividade ", "prepara-nos para enfrentar situações atípicas decorrentes ", "maximiza as possibilidades por conta ", "desafia a capacidade de equalização ", "agrega valor ao estabelecimento ", "é uma das consequências ", "promove a alavancagem ", "não pode mais se dissociar ", "possibilita uma melhor visão global ", "estimula a padronização ", "aponta para a melhoria ", "faz parte de um processo de gerenciamento ", "causa impacto indireto na reavaliação ", "apresenta tendências no sentido de aprovar a manutenção ", "estende o alcance e a importância ", "deve passar por modificações independentemente ", "afeta positivamente a correta previsão "],
        ["das condições financeiras e administrativas exigidas.", "das diretrizes de desenvolvimento para o futuro.", "do sistema de participação geral.", "das posturas dos órgãos dirigentes com relação às suas atribuições.", "das novas proposições.", "das direções preferenciais no sentido do progresso.", "do sistema de formação de quadros que corresponde às necessidades.", "das condições inegavelmente apropriadas.", "dos índices pretendidos.", "das formas de ação.", "dos paradigmas corporativos.", "dos relacionamentos verticais entre as hierarquias.", "do processo de comunicação como um todo.", "dos métodos utilizados na avaliação de resultados.", "de todos os recursos funcionais envolvidos.", "dos níveis de motivação departamental.", "da gestão inovadora da qual fazemos parte.", "dos modos de operação convencionais.", "de alternativas às soluções ortodoxas.", "dos procedimentos normalmente adotados.", "dos conhecimentos estratégicos para atingir a excelência.", "do fluxo de informações.", "do levantamento das variáveis envolvidas.", "das diversas correntes de pensamento.", "do impacto na agilidade decisória.", "das regras de conduta normativas.", "do orçamento setorial.", "do retorno esperado a longo prazo.", "do investimento em reciclagem técnica.", "do remanejamento dos quadros funcionais."] ]

    print(r[0][randint(0, len(r[0]) - 1)] + r[1][randint(0, len(r[1]) - 1)] + r[2][randint(0, len(r[2]) - 1)] + r[3][randint(0, len(r[3]) - 1)])

def f2():

    r = [ ["De acordo com a segunda tópica freudiana, ", "A doutrina de Lacan sobre o RSI diz que ", "Freud, em correspondência a Jung, cita que ", "É imperioso ressaltar que ", "A clínica mostra que o início do tratamento ", "Cada inconsciente relativo confunde-se, por meio de uma redução operacional, com ", "Quando dizemos ao paciente que certa imagem sua significa outra coisa, ", "Ao mesmo tempo e de maneira simétrica, ", "Freud disse que ", "Lacan dirá que ", "Não fosse uma claudicação, ", "A exterioridade que vige no mais íntimo de nós mesmos, carrega ", "O assujeitamento ao Outro reprime ", "A psicanálise parte da idéia de que ", "Enquanto conceito psicanalítico, ", "O desejo portanto, ", "O sonho é a realização de um desejo que ", "A pulsão é o elo entre o somático e o psíquico onde ", "Assim, ", "Por outro lado, ", "Do mesmo modo, ", "Ora, ", "Podemos descrever, assim, ", "Não hesitamos em comparar que ", "Compreendemos cedo que ", "Não conseguindo descartar complexos pessoais, ", "Mais além do princípio de prazer, ", "Não-todo fálico, "],
        ["o nó borromeano que amarra a tripartição estrutural dos registros real, simbólico e imaginário ", "a onipresença das fantasias subjacentes ", "os processos oníricos e, por extensão, todo o inconsciente ", "o movimento da pulsão escópica ", "o estado amoroso na hipnose ", "o limite teórico das ruturas de campo interpretativas ", "a nossa subjetivação ", "o pai totêmico da horda primeva ", "o repúdio ao feminino ", "o recalque da enunciação ", "o desejo inconsciente ", "o delírio ligado à produção de um certo saber, ", "a ausência de autoridade ", "uma parte valiosa e bem dotada da sociedade ", "um exaltado sem organização e nem disciplina ", "o princípio suscetível que serve de base ", "a tendência sexual inibida ", "a foraclusão do significante do Nome-do-Pai ", "o polo hostil da ambivalência afetiva do complexo paterno ", "o inconsciente estruturado como linguagem ", "a pulsão escópica ", "o assédio das grandes necessidades orgânicas ", "a defesa frente à inexorabilidade do real "],
        ["é o ponto de fundação de nosso próprio desejo ", "aferra o desejo à Coisa ", "opera não per via di porre, e sim per via di levare ", "modifica a intervenção ", "já está implícito no uso contemporâneo da interpretação transferencial ", "produz uma marca psíquica ", "vela a enunciação ", "recusa a castração ", "constrói um delírio ", "denega a natureza do sofrimento ", "realiza a travessia da fantasia ", "contribui para a colocação em cena ", "fornece a dimensão teórica ", "se acompanha então de inconvenientes não negligenciáveis ", "foraclui o ponto de fundação ", "se vale da tradução metafórica do material "],
        ["sem que isso impeça a extração de gozo.", "que delimita o campo de intervenção do analista ", "que termina por transformar o objeto em uma instância paranóica.", "que leva à convergência no recalque.", "cujos efeitos produzem o recalque desta mesma etilogia sexual da neurose.", "que faz com que o sujeito se constitua no campo do Outro.", "cujo o eu não é senhor em sua própria casa.", "quando a angústia é sem objeto.", "que não há Outro do Outro.", "que não há metalinguagem.", "que não há relação sexual.", "que a Mulher não existe.", "que define o modo de relação do sujeito com o seu sofrimento.", "cuja resistência é sempre do analista", 'da nostalgia da suposta presença da "Coisa" que teria nos salvado do desamparo.', "que supostamente nos faria pleno.", "que deixa brotar de si o Homem Psicanalítico.", "revelando-se por fim que o sofrimento em si mesmo é um gozo"] ]

    print(r[0][randint(0, len(r[0]) - 1)] + r[1][randint(0, len(r[1]) - 1)] + r[2][randint(0, len(r[2]) - 1)] + r[3][randint(0, len(r[3]) - 1)])

def f3():

    r = [ ["Fala pro cliente que ", "Com este commit, ", "Nesse pull request, ", "Dado o fluxo de dados atual, ", "Explica pro Product Onwer que ", "Desde ontem a noite ", "A equipe de suporte precisa saber que "],
        ["a normalização da data ", "um erro não identificado ", "o gerenciador de dependências do frontend ", "o módulo de recursão paralela ", "a otimização de performance da renderização do DOM ", "a disposição dos elementos HTML ", "a compilação final do programa ", "o deploy automatizado no Heroku ", "o último pull request desse SCRUM "],
        ["deletou todas as entradas ", "otimizou a renderização ", "causou o bug ", "corrigiu o bug ", "superou o desempenho ", "complexificou o merge ", "facilitou a resolução de conflito ", "causou a race condition "],
        ["do nosso servidor de DNS.", "do polimorfismo aplicado nas classes.", "do fluxo de dados de forma retroativa no server.", "de estados estáticos nos componentes da UI.", "do JSON compilado a partir de proto-buffers.", "de uma compilação com tempo acima da media.", "de uma configuração Webpack eficiente nos builds.", "da execução parelela de funções em multi-threads.", "de compilação multi-plataforma de forma asincrona.", "da execução de requisições effcientes na API.", "na estabilidade do protocolo de transferência de dados.", "do carregamento de JSON delimitado por linhas.", "na interpolação dinâmica de strings.", "no parse retroativo do DOM.", "no fechamento automático das tags.", "na compilação de templates literais.", "na definição de variaveis com tipos estáticos.", "da renderização de floats parciais.", "na organização alfanumérico dos arrays multidimensionais", "dos parametros passados em funções privadas.", "dos argumentos que definem um schema dinâmico.", "na criação de novos polyfills para suportar os processos."] ]

    print(r[0][randint(0, len(r[0]) - 1)] + r[1][randint(0, len(r[1]) - 1)] + r[2][randint(0, len(r[2]) - 1)] + r[3][randint(0, len(r[3]) - 1)])

if __name__ == '__main__':
    main()