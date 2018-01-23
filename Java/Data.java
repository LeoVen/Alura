/*
 * Doctype         : Example
 * Created by      : Leonardo Vencovsky
 * Together with   : niemand / ninguém / nadie / nobody ~~~~~~
 * Date            : 19/01/2018
 * Last modified   : 21/01/2018
 * Editor          : Sublime Text 3
 * Inspiration     : Alura [www.alura.com.br]  Java I : Primeiros Passos aula 05 & aula 07
 * Language        : Portuguese
 *
 * Classe pegada e editada da Alura
 *
*/

public class Data {
    private int dia;
    private int mes;
    private int ano;
    private String aux_dia;
    private String aux_mes;

    public Data(int dia, int mes, int ano) {
        this.dia = dia;
        this.mes = mes;
        this.ano = ano;

        if (! isDataViavel(dia, mes, ano)) {
            System.out.println("A data " + formata() + " não existe!");
        }
    }

    public String formata() {
        return this.dia+"/"+this.mes+"/"+this.ano;
    }

    public String getStringData() {

        if (this.dia < 10) {
            this.aux_dia = "0";
        } else {
            this.aux_dia = "";
        }
        if (this.mes < 10) {
            this.aux_mes = "0";
        } else {
            this.aux_mes = "";
        }
        return this.aux_dia + this.dia + "/" + this.aux_mes + this.mes + "/" + this.ano;
    }

    private boolean isDataViavel(int dia, int mes, int ano) {
        if (dia <= 0 || mes <= 0) {
            return false;
        }

        int ultimoDiaDoMes = 31; // por padrao são 31 dias
        if (mes == 4 || mes == 6 || mes == 9 || mes == 11 ) {
            ultimoDiaDoMes = 30;
        } else if (mes == 2) {
            ultimoDiaDoMes = 28;
            if((ano % 400 == 0) || ((ano % 4 == 0) && (ano % 100 != 0))){
                ultimoDiaDoMes = 29;
            }
        }
        if (dia > ultimoDiaDoMes) {
            return false;
        }

        return true;
    }
}