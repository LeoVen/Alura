package br.com.lux.hibernate.util;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;

public class JPAUtil {

	private static EntityManagerFactory emf = Persistence.createEntityManagerFactory("oracle");
	
	public EntityManager getEntityManager() {
		return emf.createEntityManager();
	}
	
}
