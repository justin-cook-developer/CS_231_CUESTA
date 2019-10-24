import java.util.Scanner;

public class Maximums {
    private static int maximum(int num1, int num2, int num3) {
        if (num1 >= num2 && num1 >= num3) {
            return num1;
        } else if (num2 >= num1 && num2 >= num3) {
            return num2;
        } else {
            return num3;
        }
    }

    public static void main( String [] args) {
        Scanner myScanner = new Scanner(System.in);

        System.out.println("Enter a number:");

        String strNum = myScanner.nextLine();

        int inputNum = Integer.parseInt(strNum);

        System.out.println(maximum(inputNum, 4, 2));
    }
}
