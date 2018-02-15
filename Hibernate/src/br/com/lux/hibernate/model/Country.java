package br.com.lux.hibernate.model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.SequenceGenerator;
import javax.persistence.Table;

@Entity
@Table(name = "COUNTRY_INFO", schema = "TESTE")
@SequenceGenerator(name = "seq", sequenceName="seq", allocationSize = 1)
public class Country {

	@Id
	@GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "seq")
	@Column(name = "RANKING")
	private int ranking;

	@Column(name = "COUNTRY")
	private String name;

	@Column(name = "POPULATION")
	private double population;

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

	public double getPopulation() {
		return population;
	}

	public void setPopulation(double population) {
		this.population = population;
	}

}
