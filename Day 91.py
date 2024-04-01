import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int Q = scanner.nextInt();
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
        
        while (Q-- > 0) {
            int x = scanner.nextInt();
            int y = scanner.nextInt();
            
            if (x == 1) {
                priorityQueue.add(y);
            } else if (x == 2) {
                if (priorityQueue.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(priorityQueue.peek());
                }
            } else if (x == 3) {
                if (!priorityQueue.isEmpty()) {
                    priorityQueue.poll();
                }
            }
        }
        
        scanner.close();
    }
}
