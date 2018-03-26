package models;

import java.util.ArrayList;
import java.util.List;

public class Course {

	private String name;
	private String instructor;
	private List<Video> videoLessons = new ArrayList<>();

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
		return videoLessons;
	}

}
