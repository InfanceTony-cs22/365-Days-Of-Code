import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int Q = scanner.nextInt();
        scanner.nextLine();
        
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        
        while (Q-- > 0) {
            int x = scanner.nextInt();
            int y = scanner.nextInt();
            
            if (x == 1) {
                pq.offer(y);
            } else if (x == 2) {
                if (!pq.isEmpty()) {
                    System.out.println(pq.peek());
                } else {
                    System.out.println(-1);
                }
            } else if (x == 3) {
                if (!pq.isEmpty()) {
                    pq.poll();
                }
            }
        }
        
        scanner.close();
    }
}
