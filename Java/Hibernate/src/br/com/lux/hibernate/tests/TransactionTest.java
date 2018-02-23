package br.com.lux.hibernate.tests;

import java.math.BigDecimal;
import java.util.Calendar;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;

import br.com.lux.hibernate.model.Account;
import br.com.lux.hibernate.model.TType;
import br.com.lux.hibernate.model.Transaction;
import br.com.lux.hibernate.util.JPAUtil;

public class TransactionTest {

	public static void main(String[] args) {
		
		Account account = new Account();
		account.setBank("Santander");
		account.setAgency("3321");
		account.setNumber("5545");
		account.setOwner("Leonardo");
		
		Transaction transaction = new Transaction();
		transaction.setDate(Calendar.getInstance());
		transaction.setDescription("Churrascaria");
		transaction.setType(TType.CREDIT);
		transaction.setValue(new BigDecimal("144.99"));
		
		transaction.setAccount(account);
		
		EntityManagerFactory emf = Persistence.createEntityManagerFactory("oracle");
		EntityManager em = emf.createEntityManager();
		em.getTransaction().begin();
		
		em.persist(account);
		em.persist(transaction);
		
		em.getTransaction().commit();
		em.close();
		
	}
	
}
