package models;

public class Video implements Comparable<Video> {

	private String title;
	private int time;

	public int getTime() {
		return time;
	}

	public String getTitle() {
		return title;
	}

	public Video(String title, int time) {
		this.title = title;
		this.time = time;
	}

	@Override
	public String toString() {
		return "[" + this.title + " : " + this.time + "]";
	}

	@Override
	public int compareTo(Video obj) {
		if (this.time < obj.getTime())
			return -1;
		else if (this.time > obj.getTime())
			return 1;
		return 0;
	}

}
