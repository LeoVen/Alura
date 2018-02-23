package br.com.lux.jdbc.tests;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class Delete {

	public static void main(String[] args) throws SQLException, ClassNotFoundException {
		Connection connection = Database.getConnection();
		connection.setAutoCommit(false);

		// Preparando o statement contra sql injection
		String sql = "delete from sugar_cane_productivity where ranking > 5";
		PreparedStatement statement = connection.prepareStatement(sql);

		int result = statement.executeUpdate();

		connection.commit();

		System.out.println(result + " registros deletados");

	}

}
