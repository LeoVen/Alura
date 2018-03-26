package tests;

import java.util.List;

import models.Course;
import models.Video;

public class CourseTest {
	public static void main(String[] args) {
		Course java1 = new Course("Java 1: Principles of Java and OOP", "Jonas Steffen");
		List<Video> vl = java1.getVideoLessons();
		System.out.println(vl);
	}
}
