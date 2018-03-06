package br.com.lux.gerenciador.web;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import br.com.lux.gerenciador.Empresa;
import br.com.lux.gerenciador.dao.EmpresaDAO;

@WebServlet(urlPatterns = "/novaEmpresa")
public class NovaEmpresa extends HttpServlet {

	private static final long serialVersionUID = 1L;

	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {

		String nome = req.getParameter("nome");
		Empresa empresa = new Empresa(nome);
		
		new EmpresaDAO().adiciona(empresa);
		
		req.setAttribute("empresa", empresa);
		RequestDispatcher dispatcher = req.getRequestDispatcher("/WEB-INF/paginas/novaEmpresa.jsp");
		dispatcher.forward(req, resp);
		
		PrintWriter writer = resp.getWriter();
		writer.println("<html><body>Empresa " + empresa.getNome() + " adicionada com sucesso </body></html>");
		
	
	}
	
}