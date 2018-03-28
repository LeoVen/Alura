/*
 * Student.java
 *
 * Luxarvum Consultoria
 *
 * Created on 28 de mar de 2018
 * by leona
 *
 * Last modified on 28 de mar de 2018
 * by leona
 *
 * Descrição sobre o que este arquivo representa.
 *
 * Notas
 *
 */
package models;

public class Student {

	private String name;
	private int age;
	private int id;

	public Student(String name, int age, Integer id) {
		if (name == null || id == null) {
			throw new NullPointerException("Name and Id can't be null");
		}
		this.id = id;
		this.name = name;
		this.age = age;
	}

	public String getName() {
		return name;
	}

	public int getAge() {
		return age;
	}

	public int getId() {
		return id;
	}

	@Override
	public boolean equals(Object obj) {
		Student s = (Student) obj;
		return this.name.equals(s.name);
	}

	@Override
	public int hashCode() {
		return this.name.hashCode();
	}

	@Override
	public String toString() {
		return "[Aluno " + this.name + ", " + this.age + " years]";
	}
}
