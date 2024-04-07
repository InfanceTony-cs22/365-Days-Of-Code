import java.util.*;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Input two numeric strings
        String str1 = scanner.nextLine();
        String str2 = scanner.nextLine();
        
        // Create BigIntegers from the input strings
        BigInteger num1 = new BigInteger(str1);
        BigInteger num2 = new BigInteger(str2);
        
        // Calculate the sum
        BigInteger sum = num1.add(num2);
        
        // Print the result
        System.out.println(sum.toString());
        
        scanner.close();
    }
}
