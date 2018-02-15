package br.com.lux.hibernate.tests;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;

import br.com.lux.hibernate.model.Finance;

public class FinanceTest {

	public static void main(String[] args) {

		Finance f = new Finance();
		f.setTitular("Leonardo");
		f.setAgencia("3354");
		f.setBanco("Santander");
		f.setNumero("229431");
		f.setId(1);

		EntityManagerFactory emf = Persistence.createEntityManagerFactory("oracle");
		EntityManager em = emf.createEntityManager();

		em.getTransaction().begin();
		em.persist(f);
		em.getTransaction().commit();

		em.close();
		emf.close();

	}

}
