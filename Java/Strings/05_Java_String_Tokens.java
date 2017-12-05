import java.io.*;
import java.util.*;
public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        s = s.trim();
        scan.close();
        int l = s.length();
        if ((0 == l))
        {
            System.out.println("0");
        }
        else
        {
            String t[] = s.split("[ !,?._'@]+");
            int tlen = t.length;
            System.out.println(tlen);
            for (int i = 0; i < tlen; i++)
            {
                System.out.println(t[i]);    
            }
        }
    }
}
