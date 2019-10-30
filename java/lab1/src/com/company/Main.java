package com.company;

public class Main {

    public static void main(String[] args) {
	    System.out.println("Numbers");

	    for (int i = 1; i <= 50; i++) {
	        System.out.println("\n--------------------\n");
	        System.out.println("Current number: " + i);

	        if (i % 2 == 0) {
	            System.out.println(i + " is even.");
            } else {
                System.out.println(i + " is odd.");
            }

            if (i % 8 == 0 && i % 3 == 0) {
                System.out.println(i + " is evenly divisible by 3 and 8.");
            } else if (i % 8 == 0) {
                System.out.println(i + " is evenly divisible by 8");
            } else if (i % 3 == 0) {
                System.out.println(i + " is evenly divisible by 3");
            } else {
                System.out.println(i + " is not evenly divisible by 3 or 8.");
            }
        }
    }
}
