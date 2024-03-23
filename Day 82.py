import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        
        // Read the first integer
        int num1 = Integer.parseInt(reader.readLine());
        
        // Read the second integer
        int num2 = Integer.parseInt(reader.readLine());
        
        // Print both integers in a space-separated manner
        System.out.println(num1 + " " + num2);
    }
}
