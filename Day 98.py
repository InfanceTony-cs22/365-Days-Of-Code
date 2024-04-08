import java.util.*;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Input
        String n = scanner.next();
        scanner.close();
        
        // Convert input string to BigInteger
        BigInteger num = new BigInteger(n);
        
        // Check if the BigInteger is prime
        if (num.isProbablePrime(10)) {
            System.out.println("prime");
        } else {
            System.out.println("not prime");
        }
    }
}
