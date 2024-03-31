import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int Q = scanner.nextInt();
        Queue<Integer> queue = new LinkedList<>();
        
        while (Q-- > 0) {
            int x = scanner.nextInt();
            int y = scanner.nextInt();
            
            if (x == 1) {
                queue.add(y);
            } else if (x == 2) {
                if (queue.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(queue.peek());
                }
            } else if (x == 3) {
                if (!queue.isEmpty()) {
                    queue.poll();
                }
            }
        }
        
        scanner.close();
    }
}
