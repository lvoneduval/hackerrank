import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int cur_n;
        ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
        for (int i = 0; i < n; i++)
        {
           ArrayList<Integer> col = new ArrayList<>(); 
           cur_n = sc.nextInt();
            for (int j = 0; j < cur_n; j++)
            {
                col.add(sc.nextInt());
            }
            arr.add(col);
        }
        n = sc.nextInt();
        for (int i = 0; i < n; i++)
        {
            int x = sc.nextInt();
            int y = sc.nextInt();
            try{
                int tmp = arr.get(x-1).get(y -1);
                System.out.println(tmp);
            }
            catch(IndexOutOfBoundsException e)
            {
                System.out.println("ERROR!");
            }
        }
    }
}
