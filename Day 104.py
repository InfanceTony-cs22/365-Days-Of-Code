import java.util.Scanner;

public class Main {

    /*
     * Complete the 'getDay' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts following parameters:
     *  1. String day
     *  2. String month
     *  3. String year
     */

    public static String getDay(String day, String month, String year) {
        int d = Integer.parseInt(day);
        int m = Integer.parseInt(month);
        int y = Integer.parseInt(year);
        
        // Create a calendar instance
        java.util.Calendar cal = java.util.Calendar.getInstance();
        cal.set(y, m - 1, d); // Month is zero-based
        
        // Get the day of the week
        int dayOfWeek = cal.get(java.util.Calendar.DAY_OF_WEEK);
        
        // Convert the day of the week to a string
        String[] daysOfWeek = {"SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"};
        String result = daysOfWeek[dayOfWeek - 1]; // Adjust for zero-based indexing
        
        return result;
    }

    public static void main(String[] args) {

        /don't alter the code below*****/
        
        Scanner in = new Scanner(System.in);
        String month = in.next();
        String day = in.next();
        String year = in.next();
        
        System.out.println(getDay(day, month, year));
        
        /******/
        
    }
}
