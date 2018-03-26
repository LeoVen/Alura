package tests;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

import models.Video;

public class ArrayListTest {

	public static void main(String[] args) {

		String str1 = "Hello World!";
		String str2 = "Lorem ipsum";
		String str3 = "I'm not a robot";

		// Declaration of ArrayList
		ArrayList<String> strList = new ArrayList<>();

		// Adding String to ArrayList of type String
		strList.add(str1);
		strList.add(str2);
		strList.add(str3);

		for (String string : strList) {
			System.out.println("String: " + string);
		}

		// Removing first element
		strList.remove(0);

		// Geting element by index
		String firstString = strList.get(0);
		System.out.println("The first element is: " + firstString);

		strList.add("Definetly not a NullPointerException!");
		strList.add("Java is ancient. Where is Java++ ?");
		strList.add("To infinity and beyond!");

		// Size of ArrayList
		for (int i = 0; i < strList.size(); i++) {
			System.out.println("String in for loop: " + strList.get(i));
		}

		System.out.println("ArrayList size: " + strList.size());

		// Foreach method in ArrayList with lambda function
		strList.forEach(str -> {
			System.out.println(str);
			System.out.println("Length: " + str.length());
		});

		// Sorting with Collections Class
		Collections.sort(strList);
		System.out.println("Sorted List: ");
		System.out.println(strList);

		// Filling up new ArrayList with MyClass
		ArrayList<Video> classList = new ArrayList<>();
		strList.forEach(str -> {
			classList.add(new Video(str, str.length()));
		});
		System.out.println(classList);

		// Sorting
		Collections.sort(classList);
		System.out.println(classList);

		// Sorting with comparator
		Collections.sort(classList, Comparator.comparing(Video::getTitle));
		System.out.println(classList);

		// Can also be done with:
		classList.sort(Comparator.comparing(Video::getTitle));
		System.out.println(classList);

	}
}
