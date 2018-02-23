package br.com.lux.hibernate.model;

import java.math.BigDecimal;
import java.util.Calendar;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.EnumType;
import javax.persistence.Enumerated;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.ManyToOne;
import javax.persistence.Table;
import javax.persistence.TableGenerator;
import javax.persistence.Temporal;
import javax.persistence.TemporalType;

@Entity
@Table(name = "TRANSACTIONS", schema = "TESTE")
@TableGenerator(name = "transaction", initialValue = 0, allocationSize = 1)
public class Transaction {

	@Id
	@GeneratedValue(strategy = GenerationType.TABLE, generator = "transaction")
	@Column(name = "tn_id")
	private Integer id;

	@Column(name = "tn_value")
	private BigDecimal value;

	@Enumerated(EnumType.STRING)
	@Column(name ="tn_type")
	private TType type;

	@Temporal(TemporalType.TIMESTAMP)
	@Column(name = "tn_date")
	private Calendar date;

	@Column(name = "tn_description")
	private String description;

	@ManyToOne
	private Account account;

	public BigDecimal getValue() {
		return value;
	}

	public void setValue(BigDecimal value) {
		this.value = value;
	}

	public TType getType() {
		return type;
	}

	public void setType(TType type) {
		this.type = type;
	}

	public Calendar getDate() {
		return date;
	}

	public void setDate(Calendar date) {
		this.date = date;
	}

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}

	public Account getAccount() {
		return account;
	}

	public void setAccount(Account account) {
		this.account = account;
	}

	public Integer getId() {
		return id;
	}

}
