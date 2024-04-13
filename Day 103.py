import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Input: Number of entries in the examination database
        int n = scanner.nextInt();
        scanner.nextLine(); // Consume newline
        
        // Create a LinkedHashMap to store student names and their total marks
        Map<String, Integer> database = new LinkedHashMap<>();
        for (int i = 0; i < n; i++) {
            String name = scanner.nextLine().trim();
            int marks = scanner.nextInt();
            scanner.nextLine(); // Consume newline
            database.put(name, marks);
        }
        
        // Input: Number of queries
        int q = scanner.nextInt();
        scanner.nextLine(); // Consume newline
        
        // Process queries
        for (int i = 0; i < q; i++) {
            String query = scanner.nextLine().trim();
            if (database.containsKey(query)) {
                System.out.println(database.get(query));
            } else {
                System.out.println("Not Found");
            }
        }
        
        scanner.close();
    }
}
