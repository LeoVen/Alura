package br.com.lux.jdbc.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import br.com.lux.jdbc.modelos.Registro;

public class RegistroDAO {

	private final Connection con;

	public RegistroDAO(Connection con) {
		this.con = con;
	}

	public void insert(Registro r) throws SQLException {
		String sql = "insert into sugar_cane_productivity values (?, ?, ?)";

		try (PreparedStatement ps = con.prepareStatement(sql)) {

			ps.setInt(1, r.getRanking());
			ps.setString(2, r.getCountry());
			ps.setDouble(3, r.getProduction());

			int result = ps.executeUpdate();

			modifiedRows(result);

		}

	}

	private static void modifiedRows(int n) {
		System.out.println(n + " rows modified");
	}

	public List<Registro> getList() throws SQLException {
		String sql = "select * from sugar_cane_productivity";
		List<Registro> registros = new ArrayList<>();

		try (PreparedStatement s = con.prepareStatement(sql)) {
			s.execute();

			try (ResultSet rs = s.getResultSet()) {
				while (rs.next()) {
					int ranking = rs.getInt("ranking");
					String country = rs.getString("country");
					double production = rs.getDouble("production");

					Registro reg = new Registro(ranking, country, production);
					registros.add(reg);
				}
			}
		}

		return registros;
	}

	public void printJoin() throws SQLException {
		String sql = "SELECT\r\n" + "t.ranking AS t_ranking, t.country AS t_country, t.production AS t_production,\r\n"
				+ "s.country AS s_country, s.ranking AS s_ranking, s.population AS s_population\r\n"
				+ "FROM sugar_cane_productivity t\r\n" + "INNER JOIN country_info s\r\n"
				+ "ON t.country = s.country ORDER BY s.ranking";

		try (PreparedStatement s = con.prepareStatement(sql)) {
			s.execute();
			try (ResultSet rs = s.getResultSet()) {
				while (rs.next()) {
					System.out.println("[ Ranking : Population : Country : Production : Ranking");
					System.out.println("[ " + rs.getInt("s_ranking") + " : " + rs.getLong("s_population") + " : "
							+ rs.getString("s_country") + " : " + rs.getInt("t_production") + " : "
							+ rs.getInt("t_ranking"));
				}
			}
		}
	}

}
