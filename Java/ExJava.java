/*
 * Doctype         : Training
 * Created by      : Leonardo Vencovsky
 * Together with   : niemand / ninguém / nadie / nobody ~~~~~~
 * Date            : 23/01/2018
 * Last modified   : 23/01/2018
 * Editor          : Sublime Text 3
 * Inspiration     : Alura [www.alura.com.br] Java II : Orientação a Objetos aula 02 (exercícios)
 * Language        : Portuguese
 *
 * Exercícios Alura
 *
 */

public class ExJava {

	public static void main(String[] args) {
		
		//Exemplos de polimorfismo
		Conta c = new Conta();
        Conta cc = new ContaCorrente();
        Conta cp = new ContaPoupanca();

        c.deposita(1000);
        cc.deposita(1000);
        cp.deposita(1000);

        System.out.println(c.getSaldo());
        System.out.println(cc.getSaldo());
        System.out.println(cp.getSaldo());

        AtualizadorDeContas adc = new AtualizadorDeContas(0.005d);

        adc.roda(c);
        adc.roda(cc);
        adc.roda(cp);

        System.out.println("===============================");
        System.out.println("Saldo total:" + adc.getSaldoTotal());

	}

}


class Conta {
	protected double saldo;

	public double getSaldo() {
		return this.saldo;
	}

	public void deposita(double valor) {
		this.saldo += valor;
	}

	public void saca(double valor) {
		if (valor > this.saldo || valor <= 0) {
			System.out.println("Saque invalido");
		} else {
			this.saldo -= valor;
			System.out.println("Saque efetuado");
		}
	}

	public void atualiza(double taxa) {
		this.saldo += this.saldo * taxa;
	}
}


class ContaCorrente extends Conta {

	public void atualiza(double taxa) {
        this.saldo += this.saldo * taxa * 2;
    }

}


class ContaPoupanca extends Conta {

	public void atualiza(double taxa) {
        this.saldo += this.saldo * taxa * 3;
    }

    public void deposita(double valor) {
        this.saldo += valor - 0.10;
    }

}


class AtualizadorDeContas {
    private double saldoTotal = 0;
    private double selic;

    public AtualizadorDeContas(double selic) {
        this.selic = selic;
    }

    public void roda(Conta c) {
        System.out.println("===============================");
        System.out.println("Saldo anterior: " + c.getSaldo());
        c.atualiza(this.selic);
        System.out.println("Saldo atualizado: " + c.getSaldo());
        this.saldoTotal += c.getSaldo();
    }

    public double getSaldoTotal() {
        return this.saldoTotal;
    }
}