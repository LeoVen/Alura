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

}
