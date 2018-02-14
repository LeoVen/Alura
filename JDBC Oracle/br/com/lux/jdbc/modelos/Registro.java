package br.com.lux.jdbc.modelos;

public class Registro {

	private Integer ranking;
	private String country;
	private double production;

	public Registro(Integer ranking, String country, double production) {
		super();
		this.ranking = ranking;
		this.country = country;
		this.production = production;
	}

	public Integer getRanking() {
		return ranking;
	}

	public void setRanking(Integer ranking) {
		this.ranking = ranking;
	}

	public String getCountry() {
		return country;
	}

	public void setCountry(String country) {
		this.country = country;
	}

	public double getProduction() {
		return production;
	}

	public void setProduction(double production) {
		this.production = production;
	}

	@Override
	public String toString() {
		return "[ " + this.getRanking() + " : " + this.getCountry() + " : " + this.getProduction() + " ]";
	}

}
