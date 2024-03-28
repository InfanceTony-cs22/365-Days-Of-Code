import java.util.*;

public class Main {
    public static void main(String[] args) {
        
        /*Dont't touch the code in this block*/
        Scanner inp = new Scanner(System.in);
        int a = inp.nextInt();
        inp.nextLine();
        int b = inp.nextInt();
        inp.nextLine();
        inp.close();
        System.out.println(add(a,b));
        System.out.println(multiply(a,b));
        /*******************************************/
    }
    
    // Function to add two integers
    public static int add(int x, int y) {
        return x + y;
    }
    
    // Function to multiply two integers
    public static int multiply(int x, int y) {
        return x * y;
    }
}
