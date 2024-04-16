import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Creating a Scanner object to read input from standard input
        Scanner scanner = new Scanner(System.in);
        
        // Reading the size of the array
        int N = scanner.nextInt();
        
        // Creating a Set to store unique elements
        Set<Integer> uniqueElements = new HashSet<>();
        
        // Reading array elements and adding them to the set
        for (int i = 0; i < N; i++) {
            int num = scanner.nextInt();
            uniqueElements.add(num);
        }
        
        // Printing the total number of unique elements
        System.out.println(uniqueElements.size());
    }
}
