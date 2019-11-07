package com.company;

public class Main {
    public static double getDiff(double[] nums) {
        double lowest = nums[0];
        double highest = nums[0];

        for (int i = 1; i < nums.length; i++) {
            double num = nums[i];

            if (num < lowest) {
                lowest = num;
            }

            if (num > highest) {
                highest = num;
            }
        }

        return highest - lowest;
    }

    public static int max(int[] nums) {
        int highest = 0;

        if (nums.length > 0) {
            highest = nums[0];
        }

        for (int i = 1; i < nums.length; i++) {
            int currentNum = nums[i];

            if (currentNum > highest) {
                highest = currentNum;
            }
        }

        return highest;
    }

    public static int[] createArr(int size) {
        int[] arr = new int[size];

        for (int i = 0; i < size; i++) {
            arr[i] = i * 10;
        }

        return arr;
    }

    public static void main(String[] args) {
        int[] nums = { 1, 3, 4 };

        double[] dubs = {1.454, 7.45, 3.88, 33.9 };

	    System.out.println(max(nums));
	    System.out.println(getDiff(dubs));

	    int[] arr = createArr(8);

	    for (int i = 0; i < arr.length; i++) {
	        System.out.println(arr[i]);
        }
    }
}
