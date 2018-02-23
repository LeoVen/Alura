package br.com.lux.hibernate.tests;

import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.Query;

import br.com.lux.hibernate.model.Country;
import br.com.lux.hibernate.util.JPAUtil;

public class TestJPQL {

	public static void main(String[] args) {
		
		PopulateDB pdb = new PopulateDB();
		pdb.populateDB();

		EntityManager em = new JPAUtil().getEntityManagerByName("orcl");
		em.getTransaction().begin();
		
		String jpql = "select c from Country c order by c.ranking";
		Query query = em.createQuery(jpql);
		
		@SuppressWarnings({ "unchecked" })
		List<Country> countries = ((List<Country>) query.getResultList());
		System.out.println(countries.size());
		for (Country c : countries) {
			System.out.println(c);
		}
		
		em.getTransaction().commit();
		em.close();

	}

}
