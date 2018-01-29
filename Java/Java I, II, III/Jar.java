/*
 * Jar e Javadoc
 *
 * Jar:
 * O Java Archive possui um conjunto de classes (e arquivos de configurações)
 * compactados, no estilo de um arquivo zip. Ele também pode ser tratado como
 * um executável se for informado qual classe deve ser a primeira a ser executada.
 * Gerando um .jar:
 *     jar -cvf NomeDoArquivo.jar br/com/nomedaempresa/projeto/pacote/*.class
 * É possível também informar mais de um pacote, separando-os com um espaço:
 *     jar -cvf NomeDoArquivo.jar br/com/empresa/projeto/pacote01/*.class br/com/empresa/projeto/pacote02/*.class 
 * Para rodar um .jar usamos a flag -jar com java:
 *     java -jar caminho/do/arquivo/Arquivo.jar
 *
 *
 */