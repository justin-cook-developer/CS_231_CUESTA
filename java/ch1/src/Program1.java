import java.util.ArrayList;

public class Program1 {
    private static double applyFormula(int a, int b) {
        return (double) (a * a + b * b + 1) / (a * b);
    }

    private static ArrayList<int[]> validIntegers() {
        ArrayList<int[]> validPairs = new ArrayList<int[]>();

        for (int b = 2; b < 1000; b++) {
            for (int a = 1; a < b; a++) {
                double x = applyFormula(a, b);

                if (x % 1 == 0) {
                    int[] pair = {b, a};
                    validPairs.add(pair);
                }
            }
        }

        return validPairs;
    }

    public static void main(String[] args) {
        ArrayList<int[]> validIntPairs = validIntegers();

        System.out.println("Valid integer pairs:");

        validIntPairs.forEach(pair -> System.out.println(pair[0] + " " + pair[1]));
    }
}