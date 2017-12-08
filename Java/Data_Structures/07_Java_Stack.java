import java.util.*;
class Solution{
   
   public static void main(String []argh)
   {
      Scanner sc = new Scanner(System.in);
      
      while (sc.hasNext()) {
         String input=sc.next();
         System.out.println(verif(input));
            //Complete the code
      }
   }
   public static boolean verif(String s)
   {
   Stack<Character> st = new Stack<>();
       int n = s.length();
       for (int i = 0; i < n ;i++)
       {
           if(!st.empty())
           {
               switch(s.charAt(i))
               {
                   case '}' : if (st.peek() == '{') {
                            st.pop();
                        } break;
                    case ']' : if (st.peek() == '[') {
                        st.pop();
                    } break;
                    case ')' : if (st.peek() == '(') {
                        st.pop();
                    } break;
                    default: st.push(s.charAt(i));
                }
           }
           else
            st.push(s.charAt(i));
       }
       return(st.empty());
   }
}
