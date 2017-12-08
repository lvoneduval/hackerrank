import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int arr[] = new int[n];
        int nb = 0;
        for (int i = 0; i < n; i++)
        {
            arr[i] = sc.nextInt();
        }
        for (int i = 0; i < n; i++)
        {
            int sum_tmp = 0;
            for (int j = i; j < n; j++)
            {
                sum_tmp += arr[j];
                if (sum_tmp < 0)
                    nb++;
            }
        }
        System.out.println(nb);
    }
}
