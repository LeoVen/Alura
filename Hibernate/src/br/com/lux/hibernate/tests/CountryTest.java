package br.com.lux.hibernate.tests;

import javax.persistence.EntityManager;

import br.com.lux.hibernate.model.Country;
import br.com.lux.hibernate.util.JPAUtil;

public class CountryTest {

	public static void main(String[] args) {

		PopulateDB pdb = new PopulateDB();
		pdb.populateDB();

		// Buscando o country por ID
		
		EntityManager em = new JPAUtil().getEntityManagerByName("oracle");
		em.getTransaction().begin();
		
		/* O estado Transient é quando uma classe ainda não passou
		 * pelo método persist(), pois se a aplicação falhar a conta
		 * ainda não está registrada no banco e suas informações
		 * serão perdidas.		 
		 */
		Country italy = new Country();
		italy.setName("Italy");
		italy.setPopulation(60494744);
		italy.setProduction(3.44);
		
		/* 
		 * Transient --> Managed
		 * 
		 */
		em.persist(italy);
		
		/* O find devolve uma instancia da classe no estado Managed
		 * onde os dados dessa classe são automaticamente alterados
		 * no banco de dados.
		*/
		Country country = em.find(Country.class, 1);
		country.setName("ChinaTown"); // Essa modificação será registrada no banco
		System.out.println(country);
		
		em.getTransaction().commit();
		
		/* Depois que fechamos o EntityManager, nenhuma das entidades
		 * será Managed. Portanto as modificações feitas após, não serão
		 * sincronizadas com o banco.
		 */
		em.close();
		
		/* Quando temos uma entidade que já foi gerenciada ela se chama
		 * Detached.
		 */
		EntityManager em2 = new JPAUtil().getEntityManagerByName("oracle");
		em2.getTransaction().begin();
		
		italy.setName("Pizza");
		
		/* Com o merge() temos que a entidade passa de Detached para
		 * Managed.
		 *             Detached ---> merge() ---> Managed
		 */
		em2.merge(italy);
		
		/* Removendo uma entidade com a função remove().
		 */
		Country c = em2.find(Country.class, 1);
		em2.remove(c);
		
		em2.getTransaction().commit();
		em2.close();
		
		/* persist() = INSERT
		 * find() = SELECT
		 * merge() = UPDATE
		 * remove() = DELETE
		 */
		
	}

}
