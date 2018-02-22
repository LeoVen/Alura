package br.com.lux.hibernate.model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;
import javax.persistence.TableGenerator;

@Entity
@Table(name = "ACCOUNTS", schema = "TESTE")
@TableGenerator(name = "account", initialValue = 0, allocationSize = 1)
public class Account {

	@Deprecated
	public Account() {
	}

	@Id
	@GeneratedValue(strategy = GenerationType.TABLE, generator = "account")
	@Column(name = "acc_id")
	private Integer id;

	@Column(name = "acc_owner")
	private String owner;

	@Column(name = "acc_bank")
	private String bank;

	@Column(name = "acc_agency")
	private String agency;

	@Column(name = "acc_number")
	private String number;

	public String getOwner() {
		return owner;
	}

	public void setOwner(String owner) {
		this.owner = owner;
	}

	public String getBank() {
		return bank;
	}

	public void setBank(String bank) {
		this.bank = bank;
	}

	public String getAgency() {
		return agency;
	}

	public void setAgency(String agency) {
		this.agency = agency;
	}

	public String getNumber() {
		return number;
	}

	public void setNumber(String number) {
		this.number = number;
	}

	public Integer getId() {
		return id;
	}

}
