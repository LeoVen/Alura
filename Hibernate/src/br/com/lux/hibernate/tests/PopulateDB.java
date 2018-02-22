package br.com.lux.hibernate.tests;

import javax.persistence.EntityManager;

import br.com.lux.hibernate.model.Country;
import br.com.lux.hibernate.util.JPAUtil;

public class PopulateDB {

	public void populateDB() {

		EntityManager em = new JPAUtil().getEntityManagerByName("oracle");

		String[] c = { "China", "India", "USA", "Indonesia", "Brazil", "Pakistan", "Mexico", "Thailand", "Colombia",
				"Australia" };
		Integer[] p = { 1409517397, 1339180127, 324459463, 263991379, 209288278, 197015955, 129163276, 69037513,
				49065615, 24450561 };
		Double[] v = { 736.11, 352.15, 126.15, 103.7, 62.83, 56.673, 36.51, 30.52, 28.6, 27.6 };

		em.getTransaction().begin();
		for (int i = 1; i <= c.length; i++) {
			Country country = new Country();
			// country.setRanking(i);
			country.setName(c[i - 1]);
			// System.out.println(c[i-1]);
			country.setPopulation(p[i - 1]);
			// System.out.println(p[i-1]);
			country.setProduction(v[i - 1]);
			em.persist(country);
		}

		em.getTransaction().commit();

		em.close();

	}

}
