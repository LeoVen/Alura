package br.com.lux.jdbc.tests;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.List;

import br.com.lux.jdbc.dao.RegistroDAO;
import br.com.lux.jdbc.modelos.Registro;

public class InsertWithDAO {

	public static void main(String[] args) throws SQLException, ClassNotFoundException {

		Registro r = new Registro(13, "Italy", 5.49);

		try (Connection con = Database.getConnection()) {
			RegistroDAO rdao = new RegistroDAO(con);
			rdao.insert(r);
			List<Registro> registros = rdao.getList();
			for (Registro registro : registros) {
				System.out.println("Existe o registro: " + registro);
			}
		}
	}
}
