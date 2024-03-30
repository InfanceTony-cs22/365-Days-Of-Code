import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> arrayList = new ArrayList<>();
        
        // Read input until a negative number is encountered
        while (scanner.hasNext()) {
            int num = scanner.nextInt();
            if (num < 0) {
                break;
            }
            arrayList.add(num);
        }
        scanner.close();
        
        // Print the ArrayList in reverse order
        for (int i = arrayList.size() - 1; i >= 0; i--) {
            System.out.print(arrayList.get(i) + " ");
        }
    }
}
