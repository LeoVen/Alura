package br.com.lux.hibernate.tests;

import javax.persistence.EntityManager;

import br.com.lux.hibernate.model.Country;
import br.com.lux.hibernate.util.JPAUtil;

public class CountryTest {

	public static void main(String[] args) {

		PopulateDB pdb = new PopulateDB();
		pdb.populateDB();

	}

}
