import static java.lang.System.in;
class Prime{
    public void checkPrime(Integer ...inte)
    {
        for (int e:inte)
        {
            if (isPrime(e)) {
                System.out.print(e + " ");
            }
        }
        System.out.println("");
    }
    boolean isPrime(int n) {
        if (n < 2) {
            return false;
        }
        for (int i = 2; i <= (int) Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
