import java.util.*;
import java.io.*;
class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            a += b;
            System.out.print(a);
            int c = 1;
            for (int j = 1; j < n; j++)
            {
                c *= 2;
                a += b * c;
                System.out.format(" %d",a);
            }
        System.out.print("\n");
        }

        in.close();
    }
}
