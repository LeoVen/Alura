package Alura1;

import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.Map;
import java.util.TreeMap;

public class Main {

    public static void main(String[] args) {

        byte myByte = Byte.MAX_VALUE;
        short myShort = Short.MAX_VALUE;
        int myInt = Integer.MAX_VALUE;
        long myLong = Long.MAX_VALUE;
        float myFloat = Float.MAX_VALUE;
        double myDouble = Double.MAX_VALUE;

        char myChar = Character.MAX_VALUE;
        String myString = "Hello World!\n";

        System.out.printf("My Int: %d\nMy Long: %d\n", myByte, myShort);
        System.out.printf("My Int: %d\nMy Long: %d\n", myInt, myLong);
        System.out.printf("My Float: %f\nMy Double: %f\n", myFloat, myDouble);
        System.out.printf("My Char: %c\nMy String: %s", myChar, myString);

        var myDecimal = new BigDecimal("3319393.424024248242333211");

        myDecimal = myDecimal.add(new BigDecimal("333.97285982342434"));

        var myInteger = new BigInteger("8283778242874181278417837273497647234");

        myInteger = myInteger.add(new BigInteger("8976487627111232323299453847112132323211"));

        System.out.println(myDecimal);
        System.out.println(myInteger);

        var myTree = new TreeMap<String, Long>();

        myTree.put("Hello", 399L);
        myTree.put("Hello", 399L);
        myTree.put("Hello", 399L);

        System.out.println("Tree Size: " + myTree.size());

        while (++myInt > 0) {
            System.out.println("Not today son");
        }

        myTree.put("Hello World!", 400L);
        myTree.put("World!", 401L);

        for (Map.Entry<String, Long> entry : myTree.entrySet()) {
            System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());
        }

        for (int i = 0; i < 10; i++) {
            System.out.print(i + " ");
        }

        System.out.println();

        do {
            myInt++;
            System.out.println(myInt);
        } while (myInt <= Integer.MIN_VALUE);

        while (true) {
            if (myLong++ < 0)
                break;

            System.out.println(myLong);
        }
    }
}
