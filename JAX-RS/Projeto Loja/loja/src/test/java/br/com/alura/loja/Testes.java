/*
	DEPRECATED
	
	SEE JAXB

 */

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

public class Testes {
	
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
		System.in.read();
		server.stop();
	}
	
	@Test
	public void main() {
		
		getCarrinho();
		postCarrinho();
		deleteCarrinho();
		alteraCarrinho();
		
	}

	public void getCarrinho() {
		
		this.content = this.target.path("/carrinhos/1").request().get(String.class);
		Carrinho carrinho = (Carrinho) new XStream().fromXML(this.content);
        Assert.assertEquals("Rua Vergueiro 3185, 8 andar", carrinho.getRua());
		
	}
	
	public void postCarrinho() {
		
		Carrinho carrinho = new Carrinho();
        carrinho.adiciona(new Produto(314L, "Tablet", 999, 1));
        carrinho.setRua("Rua Vergueiro");
        carrinho.setCidade("Sao Paulo");
        String xml = carrinho.toXML();

        Entity<String> entity = Entity.entity(xml, MediaType.APPLICATION_XML);

        Response response = target.path("/carrinhos").request().post(entity);	// POST
        Assert.assertEquals(201, response.getStatus());
		
	}
	
	public void deleteCarrinho() {
		
		Response response = target.path("/carrinhos/1/produtos/3467").request().delete();
		Assert.assertEquals(200, response.getStatus());
		
	}
	
	public void alteraCarrinho() {
		
		this.content = this.target.path("/carrinhos/1").request().get(String.class);
		Carrinho carrinho = (Carrinho) new XStream().fromXML(this.content);
		List<Produto> produtos = carrinho.getProdutos();
		Produto produto = produtos.get(0);
		
		produto.setQuantidade(11);
		
		String xml = produto.toXML();
		
		Entity<String> entity = Entity.entity(xml, MediaType.APPLICATION_XML);
		Response response = target.path("/carrinhos/1/produtos/6237/quantidade").request().put(entity);
		Assert.assertEquals(200, response.getStatus());
		
	}
	
	public void postProduto() {
		
		Produto produto = new Produto(2361, "Computador", 3459.99, 2);
		String xml = produto.toXML();
		
		Entity<String> entity = Entity.entity(xml, MediaType.APPLICATION_XML);

        Response response = target.path("/carrinhos/1/adicionar").request().post(entity);	// POST
        Assert.assertEquals(201, response.getStatus());
		
	}
	
}