import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        BitSet b[] = new BitSet[2];
        b[0] = new BitSet(n);
        b[1] = new BitSet(n);
        for (int i = 0; i < m; i++)
        {
            String query = sc.next();
            int v1 = sc.nextInt();
            int v2 = sc.nextInt();
            switch (query)
            {
                case ("AND"):
                    b[v1 - 1].and(b[v2 -1]);
                    break;  
                     
                case ("OR"):
                    b[v1 - 1].or(b[v2 -1]);
                    break;  
                
                case ("XOR"):
                    b[v1 - 1].xor(b[v2 -1]);
                    break;  
                
                case ("SET"):
                    b[v1 - 1].set(v2);
                    break;  
                
                case ("FLIP"):
                    b[v1 - 1].flip(v2);
                    break;  
            }
            System.out.format("%d %d\n", b[0].cardinality(), b[1].cardinality());
        }
    }
}
