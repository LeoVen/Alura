package models;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.NoSuchElementException;
import java.util.Set;
import java.util.TreeSet;

public class Course {

	private String name;
	private String instructor;
	private List<Video> videoLessons = new ArrayList<>();
	private Set<Student> students = new TreeSet<>(Comparator.comparing(Student::getName));
	private Map<Integer, Student> enrolled = new HashMap<>();

	public Course(String name, String instructor) {
		this.name = name;
		this.instructor = instructor;
	}

	public String getName() {
		return name;
	}

	public String getInstructor() {
		return instructor;
	}

	public List<Video> getVideoLessons() {
		return Collections.unmodifiableList(videoLessons);
	}

	public void add(Video video) {
		videoLessons.add(video);
	}

	public int getTotalTime() {
		return this.videoLessons.stream().mapToInt(Video::getTime).sum();
	}

	@Override
	public String toString() {
		return "[Course " + this.name + " : " + this.getTotalTime() + " ]" + "\nVideo Lessons:\n" + this.videoLessons;
	}

	public void enroll(Student student) {
		this.students.add(student);
		this.enrolled.put(student.getId(), student);
	}

	public Set<Student> getStudents() {
		return Collections.unmodifiableSet(this.students);
	}

	public void displayStudents() {
		System.out.println("Enrolled Students: ");
		if (this.getStudents().isEmpty()) {
			System.out.println("[ EMPTY ]");
		} else {
			this.getStudents().forEach(a -> {
				System.out.println(a);
			});
		}
	}

	public boolean isEnrolled(Student student) {
		return this.students.contains(student);
	}

	public Student getStudent(int id) {
		if (!enrolled.containsKey(id))
			throw new NoSuchElementException("There is no student with id " + id);
		return enrolled.get(id);
	}

}
