package br.com.lux.jdbc.tests;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class CommitRollback {

	public static void main(String[] args) throws SQLException, ClassNotFoundException {

		// Preparing
		String[] country = { "Brazil", "India", "China", "Thailand", "Pakistan", "Mexico", "Colombia", "Australia",
				"Indonesia", "USA" };
		double production[] = { 736.11, 352.15, 126.15, 103.7, 62.83, 56.673, 36.51, 30.52, 28.6, 27.6 };
		int result = 0;

		Connection connection = Database.getConnection();
		connection.setAutoCommit(false);

		try {
			String sql = "drop table sugar_cane_productivity";
			PreparedStatement statement = connection.prepareStatement(sql);
			statement.executeUpdate();

			sql = "CREATE TABLE sugar_cane_productivity (\r\n" + "ranking int NOT NULL,\r\n"
					+ "country varchar (20) NOT NULL,\r\n" + "production float NOT NULL,\r\n"
					+ "PRIMARY KEY (ranking)\r\n" + ")";
			statement = connection.prepareStatement(sql);
			statement.executeUpdate();

			for (int i = 0; i < 10; i++) {
				sql = "insert into sugar_cane_productivity (ranking, country, production) values (?, ?, ?)";
				statement = connection.prepareStatement(sql);
				statement.setInt(1, i + 1);
				statement.setString(2, country[i]);
				statement.setDouble(3, production[i]);
				result += statement.executeUpdate();
			}

			connection.commit();

		} catch (Exception e) {
			result = 0;
			e.printStackTrace();
			connection.rollback();
		}

		connection.close();

		System.out.println(result + " registros foram modificados");

	}

}