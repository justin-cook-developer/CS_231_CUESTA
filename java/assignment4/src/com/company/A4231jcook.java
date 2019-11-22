package com.company;

import java.util.Scanner;
import java.util.ArrayList;

public class A4231jcook {
    public static void fillArrayList(ArrayList<Integer> nums)
    {
        System.out.println("Enter a line of input with any number of integers");
        System.out.println("Enter a blank line to stop inputting");
        System.out.println("All values must be white-space-delimited");
        System.out.println("Non-integers will be discarded:");

        Scanner in = new Scanner(System.in);

        try
        {
            String line = in.nextLine();

            while (!line.equals(""))
            {
                Scanner inputs = new Scanner(line);

                while (inputs.hasNextInt())
                    nums.add(inputs.nextInt());

                line = in.nextLine();
            }
        }
        catch (Exception e)
        {
            // if no nums in ArrayList, alert user of error
            // else, proceed as usual
            if (nums.size() == 0)
            {
                System.out.println("There was an error while taking input.");
                e.printStackTrace();
            }
        }
    }

    public static double average(ArrayList<Integer> nums)
    {
        double sum = 0.0;

        for (int num : nums)
            sum += num;

        return sum / nums.size();
    }

    public static int[] minMax(ArrayList<Integer> nums)
    {
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        for (int num : nums)
        {
            if (num < min)
                min = num;

            if (num > max)
                max = num;
        }

        return new int[] { min, max };
    }

    public static void selectionSort(ArrayList<Integer> nums)
    {
        int len = nums.size();

        for (int i = 0; i < len; i++)
        {
            int minIdx = i;

            for (int j = i + 1; j < len; j++)
            {
                if (nums.get(j) < nums.get(minIdx))
                    minIdx = j;
            }

            int temp = nums.get(minIdx);

            nums.set(minIdx, nums.get(i));
            nums.set(i, temp);
        }
    }

    public static int[] mode(ArrayList<Integer> nums)
    {
        int _mode = nums.get(0);
        int modeFreq = 1;

        int testMode = nums.get(0);
        int testFreq = 1;

        for (int i = 1; i < nums.size(); i++)
        {
            int num = nums.get(i);

            if (num == _mode)
            {
                modeFreq++;
            }
            else if (num == testMode)
            {
                testFreq++;

                if (testFreq > modeFreq)
                {
                    _mode = testMode;
                    modeFreq = testFreq;
                }
            }
            else
            {
                testMode = num;
                testFreq = 1;
            }
        }

        return new int[] { _mode, modeFreq };
    }

    public static void main(String[] args) {
	    ArrayList<Integer> nums = new ArrayList<Integer>();

	    fillArrayList(nums);

	    if (nums.size() == 0)
        {
            System.out.println("No integers were entered. " +
                    "Please run the program again.");
            return;
        }

	    selectionSort(nums);

        int[] minMax = minMax(nums);
        double average = average(nums);
        int[] modeAndFrequency = mode(nums);

        System.out.println(minMax[0]);
        System.out.println(minMax[1]);

        System.out.println(average);

        System.out.println(modeAndFrequency[0]);
        System.out.println(modeAndFrequency[1]);
    }
}
