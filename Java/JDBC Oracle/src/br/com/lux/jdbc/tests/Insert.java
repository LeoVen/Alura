package br.com.lux.jdbc.tests;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class Insert {

	public static void main(String[] args) throws SQLException, ClassNotFoundException {

		Connection connection = Database.getConnection();
		String sql = "insert into sugar_cane_productivity (ranking, country, production) values (?, ?, ?)";
		PreparedStatement statement = connection.prepareStatement(sql);

		int ranking = 11;
		String country = "Africa do Sul";
		double production = 13.48;

		statement.setInt(1, ranking);
		statement.setString(2, country);
		statement.setDouble(3, production);

		int result = statement.executeUpdate();

		ranking = 12;
		country = "Germany";
		production = 9.96;

		statement.setInt(1, ranking);
		statement.setString(2, country);
		statement.setDouble(3, production);

		result += statement.executeUpdate();

		System.out.println(result + " registros foram modificados");

		statement.close();
		connection.close();

	}

}