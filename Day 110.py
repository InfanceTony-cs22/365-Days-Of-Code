import java.util.*;

class pair implements Comparable<pair> {
    int first;
    int second;

    // Parameterized constructor
    public pair(int a, int b) {
        this.first = a;
        this.second = b;
    }

    // Comparator interface for sorting in Scaler Sorted Order
    public int compareTo(pair p) {
        // Compare second attributes in decreasing order
        if (this.second != p.second) {
            return Integer.compare(p.second, this.second);
        } else {
            // If second attributes are equal, compare first attributes in decreasing order
            return Integer.compare(p.first, this.first);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        ArrayList<pair> arr = new ArrayList<pair>();
        int n = in.nextInt();
        in.nextLine();
        for (int i = 0; i < n; i++) {
            int a = in.nextInt();
            int b = in.nextInt();
            arr.add(new pair(a, b));
            in.nextLine();
        }
        in.close();
        Collections.sort(arr);
        for (int i = 0; i < n; i++) {
            System.out.println(arr.get(i).first + " " + arr.get(i).second);
        }
    }
}
