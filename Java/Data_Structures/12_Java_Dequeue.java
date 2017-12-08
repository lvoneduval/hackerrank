    import java.util.*;
    public class test {
        public static void main(String[] args) {
            Scanner in = new Scanner(System.in);
            Deque<Integer> deque = new ArrayDeque<>();
            int n = in.nextInt();
            int m = in.nextInt();
            int max = 0;
            HashSet<Integer> set = new HashSet<>();
            for (int i = 0; i < n; i++) {
                int num = in.nextInt();
                deque.addLast(num);
                set.add(num);
                if(	deque.size() == m)
                {
                    max = set.size() > max ?  set.size() : max;
                    int tmp = deque.pop();
                    if (! deque.contains(tmp)) set.remove(tmp);
                }
            }
            System.out.println(max);
        }
    }
