/*
 * StudentTest.java
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
package tests;

import java.util.Iterator;
import java.util.Set;
import java.util.Vector;

import models.Course;
import models.Student;
import models.Video;

public class StudentTest {

	public static void main(String[] args) {
		Course javaCollections = new Course("Java Collections", "Arnold Buerz");
		javaCollections.displayStudents();
		javaCollections.add(new Video("ArrayLists", 30));
		javaCollections.add(new Video("LinkedLists", 25));
		javaCollections.add(new Video("HashSets", 50));
		javaCollections.add(new Video("Maps", 40));

		Student s1 = new Student("Alan Turing", 33, 1);
		Student s2 = new Student("Grace Hopper", 55, 2);
		Student s3 = new Student("Maya Houst", 22, 3);

		javaCollections.enroll(s1);
		javaCollections.enroll(s2);
		javaCollections.enroll(s3);

		javaCollections.displayStudents();

		System.out.println(javaCollections.isEnrolled(s1));
		Student s1_c = new Student("Alan Turing", 35, 4);
		System.out.println(javaCollections.isEnrolled(s1_c));

		// What makes one equals another is their name
		System.out.println(s1_c.hashCode() == s1.hashCode());

		javaCollections.enroll(new Student("Barbara Ross", 25, 5));

		javaCollections.displayStudents();

		// Legacy

		// Iterator
		System.out.println("\nUsing iterator:");
		Set<Student> s = javaCollections.getStudents();
		Iterator<Student> it = s.iterator();
		while (it.hasNext()) {
			System.out.println(it.next());
		}

		// Vector is thread safe
		Vector<String> vector = new Vector<>();
		vector.add("Hello World");

	}
}
