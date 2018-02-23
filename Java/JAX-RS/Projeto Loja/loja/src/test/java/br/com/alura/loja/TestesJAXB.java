package br.com.alura.loja;

import java.io.IOException;
import java.util.List;

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.client.WebTarget;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

import org.glassfish.grizzly.http.server.HttpServer;
import org.glassfish.jersey.client.ClientConfig;
import org.glassfish.jersey.filter.LoggingFilter;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import com.thoughtworks.xstream.XStream;

import br.com.alura.loja.modelo.Carrinho;
import br.com.alura.loja.modelo.Produto;
import junit.framework.Assert;

public class TestesJAXB {
	
	private HttpServer server;
	private WebTarget target;
	private Client client;
	private String content;
	private ClientConfig config;

	@Before
	public void startServer() {
		server = Server.serverStart();
		this.config = new ClientConfig();
		config.register(new LoggingFilter());
		this.client = ClientBuilder.newClient(config);
		this.target = client.target("http://localhost:8080");
	}

	@After
	public void after() throws IOException {
		//System.in.read();
		server.stop();
	}
	
	@Test
	public void main() {
		
		getCarrinho();
		postCarrinho();
		deleteCarrinho();
		alteraCarrinho();
		putProduto();
		
	}

	public void getCarrinho() {
		
		Carrinho carrinho = this.target.path("/carrinhos/1").request().get(Carrinho.class);
        Assert.assertEquals("Rua Vergueiro 3185, 8 andar", carrinho.getRua());
		
	}
	
	public void postCarrinho() {
		
		Carrinho carrinho = new Carrinho();
        carrinho.adiciona(new Produto(314L, "Tablet", 999, 1));
        carrinho.setRua("Rua Vergueiro");
        carrinho.setCidade("Sao Paulo");

        Entity<Carrinho> entity = Entity.entity(carrinho, MediaType.APPLICATION_XML);

        Response response = target.path("/carrinhos").request().post(entity);	// POST
        Assert.assertEquals(201, response.getStatus());
		
	}
	
	public void deleteCarrinho() {
		
		Response response = target.path("/carrinhos/1/produtos/3467").request().delete();
		Assert.assertEquals(200, response.getStatus());
		
	}
	
	public void alteraCarrinho() {
		
		Carrinho carrinho = this.target.path("/carrinhos/1").request().get(Carrinho.class);
		List<Produto> produtos = carrinho.getProdutos();
		Produto produto = produtos.get(0);
		
		produto.setQuantidade(11);
		
		Entity<Produto> entity = Entity.entity(produto, MediaType.APPLICATION_XML);
		Response response = target.path("/carrinhos/1/produtos/6237/quantidade").request().put(entity);
		Assert.assertEquals(200, response.getStatus());
		
	}
	
	public void putProduto() {
		
		Produto produto = new Produto(2361, "Computador", 3459.99, 2);
		
		Entity<Produto> entity = Entity.entity(produto, MediaType.APPLICATION_XML);

        Response response = target.path("/carrinhos/1/adicionar").request().put(entity);
        Assert.assertEquals(201, response.getStatus());
		
	}
	
}
