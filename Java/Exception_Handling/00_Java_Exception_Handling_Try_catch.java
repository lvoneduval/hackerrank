import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x;
        int y;
        try {
            x = sc.nextInt();
            y = sc.nextInt();
            System.out.println((int)x/y);
        }catch(InputMismatchException e){
            System.out.println(e.getClass().getName());
        }catch(Exception e)
        {
            System.out.println(e);
        }
    }
}
