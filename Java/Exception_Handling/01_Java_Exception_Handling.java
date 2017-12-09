class MyCalculator {
     public static int power(int n, int p) throws Exception 
     {
         if (p < 0 || n < 0)
         {
             throw new Exception ("n or p should not be negative.");
         }
         else if (p == 0 && n ==0)
         {
             throw new Exception ("n and p should not be zero.");
         }
         else
             return((int)Math.pow(n,p));
     }
}
