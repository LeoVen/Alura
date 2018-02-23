package br.com.lux.hibernate.util;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;

public class JPAUtil {
	
	public EntityManager getEntityManagerByName(String name) {
		return Persistence.createEntityManagerFactory(name).createEntityManager();
	}

}
