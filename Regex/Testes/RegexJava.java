import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class RegexJava {

	public static void main(String[] args) {
		
		Pattern pattern = Pattern.compile("(\\d\\d)(\\w)");

		Matcher matcher = pattern.matcher("11a22b33c44d55e");

		while (matcher.find()) {

			String match = matcher.group();
			String g1 = matcher.group(1);
			String g2 = matcher.group(2);
			int start = matcher.start();
			int end = matcher.end();

			System.out.printf("%s | %s | %s [%d, %d] \n", match, g1, g2, start, end);

		}

		System.out.println("");
		String data = "2018-02-08";
		System.out.println(data);
		data = data.replaceAll("-", "/");
		System.out.println(data);

	}

}