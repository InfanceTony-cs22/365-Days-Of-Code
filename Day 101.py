import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Input string A
        String A = scanner.nextLine();
        
        // Input indices L and R
        int L = scanner.nextInt();
        int R = scanner.nextInt();
        
        scanner.close();
        
        // Print the substring from index L to index R
        System.out.println(A.substring(L, R + 1));
    }
}
