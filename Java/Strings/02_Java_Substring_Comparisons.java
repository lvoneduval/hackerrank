import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
  
    public static String getSmallestAndLargest(String s, int k) {
        String smallest = s.substring(0,k);
        String largest = s.substring(0,k);
        int len = s.length();
        String tmp = "";
        for (int i = 1; i <= len - k;i++)
        {
            tmp = s.substring(i,i+k);
            if (smallest.compareTo(tmp) > 0 )
                smallest = tmp;
            if (largest.compareTo(tmp) < 0)
                largest = tmp;
        }
        return smallest + "\n" + largest;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}
