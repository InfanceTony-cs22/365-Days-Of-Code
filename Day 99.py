import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Input
        String A = scanner.nextLine();
        String B = scanner.nextLine();
        scanner.close();
        
        // Sum the lengths of A and B
        int sumLengths = A.length() + B.length();
        System.out.println(sumLengths);
        
        // Determine if A is lexicographically greater than B
        if (A.compareTo(B) > 0) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
        
        // Capitalize the complete string A and B
        String capitalizedA = A.toUpperCase();
        String capitalizedB = B.toUpperCase();
        System.out.println(capitalizedA + " " + capitalizedB);
    }
}
