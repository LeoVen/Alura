package br.com.lux.jdbc.tests;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class ConnectionPool {

	public static void main(String[] args) throws SQLException, ClassNotFoundException {

		Database database = new Database();

		for (int i = 0; i < 100; i++) {
			Connection connection = database.getConnectionPool();

			Statement statement = connection.createStatement();

			// o método execute devolve true quando seu resultado é um ResultSet e false
			// caso contrário (update, delete etc) ou caso nenhum valor seja retornado
			if ((boolean) statement.execute("select * from sugar_cane_productivity")) {
				ResultSet resultSet = statement.getResultSet();
				while (resultSet.next()) {

					int ranking = resultSet.getInt("ranking");
					String country = resultSet.getString("country");
					float production = resultSet.getFloat("production");

					System.out.println(ranking + ": " + country + ": " + production);

				}

				resultSet.close();
			}

			statement.close();

			connection.close();
		}

	}

}