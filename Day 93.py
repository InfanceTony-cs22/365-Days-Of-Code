import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Input the size of the matrix
        int N = scanner.nextInt();
        int M = scanner.nextInt();
        
        // Initialize the matrix
        int[][] matrix = new int[N][M];
        
        // Input the matrix elements
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                matrix[i][j] = scanner.nextInt();
            }
        }
        
        // Calculate and print the column-wise sums
        for (int j = 0; j < M; j++) {
            int sum = 0;
            for (int i = 0; i < N; i++) {
                sum += matrix[i][j];
            }
            System.out.print(sum + " ");
        }
        
        scanner.close();
    }
}
