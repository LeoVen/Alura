package br.com.lux.gerenciador.web;

//import java.io.IOException;
import java.util.Collection;

//import javax.servlet.RequestDispatcher;
//import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
//import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import br.com.lux.gerenciador.Empresa;
import br.com.lux.gerenciador.dao.EmpresaDAO;

@WebServlet(urlPatterns = "/busca")
public class GetEmpresas implements Tarefa {

//	private static final long serialVersionUID = 42L;

//	@Override
//	public void init() throws ServletException {
//		super.init();
//		System.out.println("Inicializando a servlet " + this);
//	}
//
//	@Override
//	public void destroy() {
//		super.destroy();
//		System.out.println("Destruindo a servlet " + this);
//	}

//	@Override
//	protected void doGet(HttpServletRequest request, HttpServletResponse response)
//			throws ServletException, IOException {
//		String filtro = request.getParameter("filtro");
//
//		Collection<Empresa> empresas = new EmpresaDAO().buscaPorSimilaridade(filtro);
//
//		request.setAttribute("empresas", empresas);
//		RequestDispatcher dispatcher = request.getRequestDispatcher("/WEB-INF/paginas/buscaEmpresa.jsp");
//		dispatcher.forward(request, response);
//
//	}
	
	@Override
	public String executa(HttpServletRequest req, HttpServletResponse resp) {
		String filtro = req.getParameter("filtro");
		String tarefa = req.getParameter("tarefa");
		Collection<Empresa> empresas = new EmpresaDAO().buscaPorSimilaridade(filtro);
		req.setAttribute("tarefa", tarefa);
		req.setAttribute("empresas", empresas);
		return "/WEB-INF/paginas/buscaEmpresa.jsp";
//		RequestDispatcher dispatcher = req.getRequestDispatcher("/WEB-INF/paginas/buscaEmpresa.jsp");
//		dispatcher.forward(req, resp);
	}

}
