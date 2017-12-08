import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> l = new ArrayList<>();
        int n = sc.nextInt();
        for (int i = 0; i < n; i++)
        {
           l.add(sc.nextInt());
        }
        int q = sc.nextInt();
        for (int i = 0; i < q; i++)
        {
            String query = sc.next();
            if (query.compareTo("Insert") == 0)
            {
                int pos = sc.nextInt();
                int val = sc.nextInt();
                l.add(pos,val);
            }
            else
            {
                int pos = sc.nextInt();
                l.remove(pos);
            }
        }
        n = l.size();
        for (int i = 0; i < n; i++)
        {
            System.out.print(l.get(i) + " ");
        }
    }
}
