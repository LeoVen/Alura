package tests;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import models.Course;
import models.Video;

public class CourseTest {
	public static void main(String[] args) {
		Course java1 = new Course("Java 1: Principles of Java and OOP", "Jonas Steffen");
		List<Video> vl = java1.getVideoLessons();
		System.out.println();

		java1.add(new Video("Java variables", 30));
		java1.add(new Video("Code Flow", 35));
		System.out.println(java1.getVideoLessons());
		System.out.println(vl);
		System.out.println(vl == java1.getVideoLessons());

		// Then this is possible:
		// java1.getVideoLessons().add(new Video("Java Collections", 70));
		// Not allowed anymore due to Collections.unmodifiableList()
		System.out.println(vl);

		// Or, with custom function add
		java1.add(new Video("Java Collections", 70));
		java1.add(new Video("Java Frameworks", 50));
		System.out.println(vl);

		List<Video> immutableList = java1.getVideoLessons();
		List<Video> list = new ArrayList<>(immutableList);
		Collections.sort(list);
		System.out.println(list);

		System.out.println(java1.getTotalTime());

		System.out.println(java1);

	}
}
