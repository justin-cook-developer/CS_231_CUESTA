// Justin Cook / justin_cook3@my.cuesta.edu
// CIS 231 / Scovil
// Lab 14

package com.company;

import java.util.Random;

public class Lab14JCoo {
    public static final int NUM_VALUES = 10;

    public static int[] randomArray(int amount)
    {
        Random random = new Random();

        int[] randomNums = new int[amount];

        for (int i = 0; i < amount; i++)
        {
            randomNums[i] = random.nextInt();
        }

        return randomNums;
    }

    public static void printArray(int[] nums, int numPerLine)
    {
        int lenNums = nums.length;

        int numLines = lenNums / numPerLine;
        int numLeftOver = lenNums % numPerLine;

        for (int startingElem = 0; startingElem < numLines * numPerLine; startingElem += numPerLine)
        {
            String line = "";

            int idxOfLastElem = startingElem + numPerLine - 1;

            for (int i = startingElem; i < startingElem + numPerLine; i++)
            {
                line += nums[i];

                if (i != idxOfLastElem)
                    line += ", ";
            }

            System.out.println(line);
        }

        if (numLeftOver > 0)
        {
            String lastLine = "";

            int idxOfLastElem = lenNums - 1;

            for (int i = lenNums - numLeftOver; i < lenNums; i++)
            {
                lastLine += nums[i];

                if (i != idxOfLastElem)
                    lastLine += ", ";
            }

            System.out.println(lastLine);
        }
    }

    public static int findLargest(int[] nums)
    {
        int largest = Integer.MIN_VALUE;

        for (int num : nums)
        {
            if (num > largest)
                largest = num;
        }

        return largest;
    }

    public static void main(String[] args) {
	    System.out.println("Justin Cook\n");

        int[] randomNums = randomArray(NUM_VALUES);

        System.out.println("The random numbers are:");

        printArray(randomNums, 4);

        System.out.println("\nThe largest number is: " + findLargest(randomNums));
    }
}
