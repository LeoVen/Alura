package br.com.lux.hibernate.model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;
import javax.persistence.TableGenerator;

@Entity
@Table(name = "COUNTRY_INFO", schema = "TESTE")
@TableGenerator(name = "Country", initialValue = 0, allocationSize = 1)
public class Country {

	@Deprecated
	public Country() {
	}

	@Id
	@GeneratedValue(strategy = GenerationType.TABLE, generator = "Country")
	@Column(name = "RANKING")
	private int ranking;

	@Column(name = "COUNTRY")
	private String name;

	@Column(name = "POPULATION")
	private long population;

	@Column(name = "PRODUCTION")
	private double production;

	public double getProduction() {
		return production;
	}

	public void setProduction(double production) {
		this.production = production;
	}

	public int getRanking() {
		return ranking;
	}

	public void setRanking(int ranking) {
		this.ranking = ranking;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public long getPopulation() {
		return population;
	}

	public void setPopulation(long population) {
		this.population = population;
	}

	@Override
	public String toString() {
		return this.ranking + ". " + this.name + ": " + this.population + " | " + this.production;
	}

}
