/*
 *
 * Trabalhando com Threads em java e usando a keyword synchronized
 *
 */

public class ThreadsJava {

	public static void main(String[] args) throws InterruptedException {

		/*

		HelloWorld hw = new HelloWorld();
		LoremIpsum li = new LoremIpsum();

		Thread t1 = new Thread(hw);
		Thread t2 = new Thread(li);

		t1.start();
		t2.start();

		*/

		// Outro problema que pode acontecer é o acesso a variáveis por duas threads diferentes
		Conta c1 = new Conta(500.0);
		FazDeposito act = new FazDeposito(c1);

		Thread t3 = new Thread(act);
		Thread t4 = new Thread(act);

		t3.start();
		t4.start();

		t3.join();
		t4.join();

		System.out.println(c1.getSaldo());

	}

}

class HelloWorld implements Runnable {

	@Override
	public void run() {
		for (int i = 0; i < 1000; i++) {
			System.out.println("Hello World");	
		}
	}

}

class LoremIpsum implements Runnable {

	@Override
	public void run() {
		for (int j = 0; j < 1000; j++) {
			System.out.println("Lorem ipsum sit amet");
		}
	}

}

class Conta {

	private String nome;
	private double saldo;

	public Conta(String nome) {
		this.nome = nome;
	}

	public Conta(String nome, double saldo) {
		this.nome = nome;
		this.saldo = saldo;
	}

	public Conta(double saldo) {
		this.saldo = saldo;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public void setSaldo(double saldo) {
		this.saldo = saldo;
	}

	public String getNome() {
		return this.nome;
	}

	public double getSaldo() {
		return this.saldo;
	}

	public synchronized void deposita(double valor) {
		this.saldo += valor;
	}

}

class FazDeposito implements Runnable {

	private Conta conta;
	public FazDeposito(Conta conta) {
		this.conta = conta;
	}

	@Override
	public void run() {
		conta.deposita(100.0);
	}

}