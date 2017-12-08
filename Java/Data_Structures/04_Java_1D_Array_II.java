import java.util.*;

public class Solution {
 private static boolean isSolvable(int m, int[] arr, int i , int n) {
        if (i < 0 || arr[i] == 1) return false;
        if ((i == n - 1) || i + m > n - 1) return true;

        arr[i] = 1;
        return isSolvable(m, arr, i + 1, n) || isSolvable(m, arr, i - 1,n) || isSolvable(m, arr, i + m,n);
    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int q = scan.nextInt();
        while (q-- > 0) {
            int n = scan.nextInt();
            int leap = scan.nextInt();
            
            int[] game = new int[n];
            for (int i = 0; i < n; i++) {
                game[i] = scan.nextInt();
            }

            System.out.println( (isSolvable(leap, game,0,n)) ? "YES" : "NO" );
        }
        scan.close();
    }
}
