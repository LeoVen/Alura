package br.com.lux.jdbc.tests;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

import oracle.ucp.jdbc.PoolDataSource;
import oracle.ucp.jdbc.PoolDataSourceFactory;

public class Database {
	
	private PoolDataSource dataSource;

	Database() throws SQLException {
		
		PoolDataSource  pds = PoolDataSourceFactory.getPoolDataSource();
		pds.setConnectionFactoryClassName("oracle.jdbc.pool.OracleDataSource");
		pds.setURL("jdbc:oracle:thin:@localhost:1521:orcl");
		pds.setUser("teste");
		pds.setPassword("teste");
		pds.setMinPoolSize(5);
	    pds.setMaxPoolSize(10);
		this.dataSource = pds;
		
	}

	public static Connection getConnection() throws SQLException, ClassNotFoundException {

		Class.forName("oracle.jdbc.driver.OracleDriver");

		String user = "teste";
		String password = "teste";
		Connection connection = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:orcl", user, password);

		return connection;
	}
	
	Connection getConnectionPool() throws SQLException {
		Connection connection = this.dataSource.getConnection();
		return connection;
	}

}
