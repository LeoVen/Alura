package br.com.lux.jdbc.tests;

import java.sql.Connection;
import java.sql.SQLException;

import br.com.lux.jdbc.dao.RegistroDAO;

public class JoinWithDAO {

	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		
		try (Connection con = Database.getConnection()) {
			RegistroDAO rd = new RegistroDAO(con);
			rd.printJoin();
		}
		
	}
	
}
