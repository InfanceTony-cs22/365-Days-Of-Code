import java.util.Scanner;
import java.util.regex.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int testCases = Integer.parseInt(in.nextLine());
        
        while(testCases > 0) {
            String pattern = in.nextLine();
            
            try {
                // Attempt to compile the pattern
                Pattern.compile(pattern);
                System.out.println("Valid");
            } catch (PatternSyntaxException e) {
                // Pattern syntax is invalid
                System.out.println("Invalid");
            }
            
            testCases--;
        }
    }
}
