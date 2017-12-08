import java.util.Comparator;
import java.util.PriorityQueue;
class Student{
    private int id;
    private String name;
    private double CGPA;
    
    public Student(int i, String nam, double cgp)
    {
        id = i;
        name = nam;
        CGPA = cgp;
        
    }
    public int getID()
    {
        return(id);
    }
    public String getName()
    {
        return(name);
    }
    public double getCGPA()
    {
        return(CGPA);
    }
}

class Priorities{
    public List<Student> getStudents(List<String> events)
    {
        List <Student> student = new ArrayList<>();
        PriorityQueue<Student> pq = new PriorityQueue<>(
    Comparator.comparing(Student::getCGPA).reversed()
    .thenComparing(Student::getName)
    .thenComparing(Student::getID));
        for(String k: events)
        {
            Scanner sc = new Scanner(k); 
            String tmp = sc.next();
            if (tmp.equals("SERVED"))
                pq.poll();
            else
            {
                String b = sc.next();
                double c = sc.nextFloat(); 
                int a  = sc.nextInt();
                pq.add(new Student(a, b , c));
            }
            sc.close();
        }
        while (! pq.isEmpty())
        {    
            Student first = pq.poll();
            student.add(first);
        }
	    return student;
    }
}
