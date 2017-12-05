import java.util.*;
import java.text.*;
public class Solution {
    public static String getDay(String day, String month, String year) {
        Calendar cal = Calendar.getInstance();
        DateFormatSymbols dfsEN = new DateFormatSymbols(Locale.ENGLISH);
        String[] dayWeekEN = dfsEN.getWeekdays();
        SimpleDateFormat ft = new SimpleDateFormat ("yyyy-MM-dd");
        Date t;
        String s = year + "-" +month + "-" + day;
        try {
            t = ft.parse(s); 
            cal.setTime(t);
        } catch (ParseException e) { 
         System.out.println("Unparseable using " + ft); 
        }
        return dayWeekEN[cal.get(Calendar.DAY_OF_WEEK)].toUpperCase();
    }
