import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

   public static void main(String[] args) {
      Scanner in = new Scanner(System.in);
      BigInteger n = in.nextBigInteger();
      System.out.println((n.isProbablePrime(100)) ? "prime": "not prime");
      in.close();
      // Write your code here.
   }
}
