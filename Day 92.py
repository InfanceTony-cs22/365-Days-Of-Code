import java.util.*;

class pair {
    int first;
    int second;
    
    public pair() {
        this.first = 10;
        this.second = 20;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);
        int a = inp.nextInt();
        inp.nextLine();
        int b = inp.nextInt();
        inp.close();
        
        pair obj  = new pair();
        System.out.println(obj.first + obj.second);
        System.out.println(a * obj.first);
        System.out.println(b * obj.second);
    }
}
