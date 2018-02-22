package br.com.lux.maven;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class TestaProduto {
	
	@Test
	public void testaProduto() {
		
		Produto produto = new Produto("Bala de chocolate", 0.10);
		
		assertEquals(0.11, produto.getPrecoComImposto(), 0.00001);
		
		System.out.println("Meu produto é " + produto.getNome() + " e custa " + produto.getPreco());
		
	}
	
}
