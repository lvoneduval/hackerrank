import java.util.*;
import java.io.*;

class Solution{
   public static void main(String []argh)
   {
      Scanner in = new Scanner(System.in);
      HashMap<String, String> m = new HashMap<>();
      int n=in.nextInt();
      in.nextLine();
      for(int i=0;i<n;i++)
      {
         String name=in.nextLine();
         String phone=in.nextLine();
         m.put(name,phone);
      }
      while(in.hasNext())
      {
         String s=in.nextLine();
         String tmp = m.get(s);
         System.out.println(tmp == null ? "Not found" : s + "=" + tmp);
      }
      
   }
}
