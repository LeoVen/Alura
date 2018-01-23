/* 
 * Status          : Training
 * Created by      : Leonardo Vencovsky
 * Together with   : niemand / ninguém / nadie / nobody ~~~~~~
 * Date            : 22/01/2018
 * Last modified   : 22/01/2018
 * Editor          : Sublime Text 3
 * Inspiration     : Youtube [https://www.youtube.com/watch?v=qqYOYIVrso0] 4.7: Introduction to Polymorphism - The Nature of Code
 * Language        : Portuguese
 *
 * Essa classe busca aprofundar as noções de Polymorphism
*/

public class Polymorphism {

	public static void main(String[] args) {
		
		Animal[] kingdom = new Animal[100];

		for (Animal i : kingdom) {
			i = new Animal();
		}

		for (int i = 0; i < kingdom.length; i++) {
			if (i % 2 == 0 && i % 4 != 0) {
				kingdom[i] = new Parrot();
			} else if (i % 3 == 0) {
				kingdom[i] = new Dog();
			} else if (i % 4 == 0) {
				kingdom[i] = new Cat();
			} else {
				kingdom[i] = new Bunny();
			}
		}

		for (Animal i : kingdom) {
			System.out.println("\n" + i.getName());
			i.jump();
		}


	}

}

class Animal {

	protected boolean hunger;
	protected boolean tired;

	protected String name = "Generic Animal";

	public Animal() {
		this.hunger = false;
		this.tired = false;
	}

	public void eat() {
		if (this.hunger) {
			System.out.println("Omn nom nom nom");
			this.hunger = false;
			return;
		} else {
			System.out.println("I'm not Hungry..");
		}
	}

	public void run() {
		System.out.println("Running!");
		this.hunger = true;
		this.tired = true;
	}

	public void sleep() {
		if (this.tired) {
			System.out.println("zzzZZZZZzzzzZZZZZzzzz");
			this.tired = false;
			return;
		} else {
			System.out.println("I'm not tired..");
		}
	}

	public void jump() {}

	public String getName() {
		return this.name;
	}

}

class Dog extends Animal {

	public Dog() {
		super();
		this.name = "Dog";
	}

	public void bark() {
		System.out.println("BARK BARK BARK");
	}

	public void jump() {
		System.out.println("I like to jump to get the food over the table");
	}

}

class Cat extends Animal {

	public Cat() {
		super();
		this.name = "Cat";
	}

	public void meow() {
		System.out.println("MEOW MEOW");
	}

	public void jump() {
		System.out.println("A quick brown cat jumps over the lazy dog");
	}

}

class Parrot extends Animal {

	public Parrot() {
		super();
		this.name = "Parrot";
	}

	public void squawk() {
		System.out.println("Squawk squawk squawk");
	}

	public void jump() {
		System.out.println("I'm a parrot and I can't jump");
	}

}

class Bunny extends Animal {

	public Bunny() {
		super();
		this.name = "Bunny";
	}

	public void eatCarrot() {
		System.out.println("Nhack Nhack eating carrot hmmmm");
	}

	public void jump() {
		System.out.println("I can't jump but I can run pretty fast!");
	}

}