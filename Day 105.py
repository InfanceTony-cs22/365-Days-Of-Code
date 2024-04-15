import java.util.*;
import java.text.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();
        
        // Create NumberFormat instances for US and India
        NumberFormat usFormat = NumberFormat.getCurrencyInstance(Locale.US);
        Locale indiaLocale = new Locale("en", "IN");
        NumberFormat indiaFormat = NumberFormat.getCurrencyInstance(indiaLocale);
        
        // Format the payment for US and India
        String usPayment = usFormat.format(payment);
        String indiaPayment = indiaFormat.format(payment);
        
        // Print the formatted payments
        System.out.println("US: " + usPayment);
        System.out.println("India: " + indiaPayment);
    }
}
