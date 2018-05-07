package alura;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.Month;
import java.time.Period;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.OptionalDouble;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.stream.Collectors;

public class Java8 {

	public static void main(String[] args) {

		/*
		 * Consumer
		 * BiConsumer
		 * Comparator
		 * Default Methods
		 * Lambdas
		 * Method Reference
		 * Streams
		 * Optional
		 * LocalDate
		 * Period
		 * DateTimeFormatter
		 * LocalDateTime
		 * 
		 * Interface Funcional
		 */
		
		List<String> palavras = new ArrayList<>();

		palavras.add("Editora Casa do Código");
		palavras.add("Alura Online");
		palavras.add("Caelum Ensinos");

		Comparator<String> bySize = new CompareStringBySize();

		// Java 7
		Collections.sort(palavras, bySize);

		// Java 8
		palavras.sort(bySize);

		System.out.println(palavras);

		// Java 7
		// for (String p : palavras) {
		// System.out.println(p);
		// }

		// Java 8
		Consumer<String> consumer = new PrintInLine();
		palavras.forEach(consumer);

		/* 
		 * Melhorando com uma classe anonima
		 * Usando calsses anonimas para quando nao vamos reaproveitar o codigo
		 */
		Consumer<String> consumerAnonymous = new Consumer<String>() {

			@Override
			public void accept(String t) {
				// TODO Auto-generated method stub

			}

		};
		
		/*
		 * A melhor composição
		 * Aqui o new Consumer é inferido assim como sua unica função (accept)
		 * portanto é possível remover o new Consumer e a declaração do método
		 */
		palavras.forEach((String s) -> {
			System.out.println(s);
		});
		
		/* Como a interface consumer possui apenas uma função que por sua vez
		 * é passado apenas um argumento, a forma mais simplificada seria:
		 * 
		 * Interface Funcional: quando uma interface possui apenas um método
		 * abstrato podendo conter outros desde que sejam do tipo default 
		 */
		palavras.forEach(s -> System.out.println(s));

		/* 
		 * É possível fazer tambem:
		 * 
		 * Obs: só funciona com Interface Funcional (1 argumento objeto)
		 */
		// Consumer stringPrinter = System.out::println;
		Consumer stringPrinter = s -> System.out.println(s);
		
		palavras.add("Python");
		palavras.add("Ruby");
		palavras.add("JavaScript");

		/*
		 * Comparator
		 */
		palavras.sort(new Comparator<String>() {

			@Override
			public int compare(String s1, String s2) {
				
				if (s1.length() < s2.length())
					return -1;
				
				if (s1.length() > s2.length())
					return 1;
				
				return 0;
			}
			
		});
		
		/*
		 * Usando uma função lambda
		 */
		palavras.sort((s1, s2) -> {
				return Integer.compare(s1.length(), s2.length());
			});
		
		/*
		 * É possível deixá-lo ainda mais enxuto
		 * Observe como não é necessário também usar o return
		 */
		palavras.sort((s1, s2) -> Integer.compare(s1.length(), s2.length()));
		
		
		/*
		 * Com Thread
		 */
		new Thread(() -> System.out.println("Executando um Runnable")).start();
		
		
		/*
		 * Method References
		 */
		palavras.sort(Comparator.comparing(s -> s.length()));
		
		/*
		 * É o mesmo que
		 */
		// Function<String, Integer> strFunction = s -> s.length();
		// Function<String, Integer> strFunction = String::length;
		Function<String, Integer> strFunction = new Function<String, Integer>() {
			@Override
			public Integer apply(String s) {
				return s.length();
			}
		};
		Comparator<String> strComparator = Comparator.comparing(strFunction);
		palavras.sort(strComparator);
		
		// Ou
		palavras.sort(Comparator.comparing(String::length));
		
		palavras.sort(String.CASE_INSENSITIVE_ORDER);

		
		/*
		 * Streams
		 * 
		 * Usando a classe Course
		 */
		System.out.println(" ");
		List<Course> courses = new ArrayList<>();
		courses.add(new Course("Python", 240));		
		courses.add(new Course("C++", 170));
		courses.add(new Course("Java", 270));
		courses.add(new Course("Perl", 80));
		courses.add(new Course("JavaScript", 260));
		
		//courses.sort(Comparator.comparing(Course::getStudents));
		//courses.forEach(c -> System.out.println(c.getName()));
		
		// A lista original não é afetada
		courses.stream()
			.filter(c -> c.getStudents() >= 200)
			.map(Course::getName)
			.forEach(System.out::println);
		
		int sum = courses.stream()
				.mapToInt(Course::getStudents)
				.sum();
		
		System.out.println("Total de alunos: " + sum);

		/*
		 * Tipos Optional	
		 */
		
		Optional<Course> optionalCourse = courses.stream()
			.filter(c -> c.getStudents() >= 300)
			.findAny();
		
		// Se encontrar, ok, caso contrário null
		Course ifCourse = optionalCourse.orElse(null);
		
		// Se existe, imprimir na tela
		optionalCourse.ifPresent(c -> System.out.println(c.getName()));
		
		OptionalDouble average = courses.stream()
			.filter(c -> c.getStudents() >= 200)
			.mapToInt(Course::getStudents)
			.average();
		
		// Obter resultado de um filtro de uma Stream
		List<Course> filteredList = courses.stream()
				.filter(c -> c.getStudents() >= 200)
				.collect(Collectors.toList());
		
		// Ou obter o resultado em outra forma de estrutura
		Map<String, Integer> coursesMap = courses.stream()
				.filter(c -> c.getStudents() >= 100)
				.collect(Collectors.toMap(
						c -> c.getName(),
						c -> c.getStudents()));
		
		// BiConsumer
		courses.stream()
				.filter(c -> c.getStudents() >= 100)
				.collect(Collectors.toMap(
						c -> c.getName(),
						c -> c.getStudents()))
				.forEach((name, students) -> System.out.println("The course "
						+ name + " has " + students + " students"));
		
		/*
		 * Datas
		 */
		LocalDate today = LocalDate.now();
		
		LocalDate birthday = LocalDate.of(1995, Month.JANUARY, 19);
		
		int month = birthday.getMonthValue();
		
		Period period = Period.between(birthday, today);
		long totalDays = ChronoUnit.DAYS.between(birthday, today);
		System.out.println(totalDays);

		DateTimeFormatter formater = DateTimeFormatter.ofPattern("dd/MM/yyyy");
		
		System.out.println(birthday.format(formater));
		
		LocalDateTime now = LocalDateTime.now();
		System.out.println(now.format(DateTimeFormatter.ofPattern("dd/MM/yyyy hh:mm:ss")));
		
	}

}

class PrintInLine implements Consumer<String> {

	@Override
	public void accept(String t) {
		System.out.println(t);
	}

}

class CompareStringBySize implements Comparator<String> {

	@Override
	public int compare(String s1, String s2) {

		if (s1.length() < s2.length())
			return -1;
		else if (s1.length() > s2.length())	
			return 1;

		return 0;
	}

}

class Course {
	
	private String name;
	private int students;
	
	public Course(String name, int students) {
		this.name = name;
		this.students = students;
	}
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getStudents() {
		return students;
	}
	public void setStudents(int students) {
		this.students = students;
	}
	
}