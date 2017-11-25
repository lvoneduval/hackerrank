class Person {
    public :
        virtual void getdata() = 0;
        virtual void putdata() = 0;
    
    protected :
        int age;
        string name;
};

class Professor : public Person{
    public :
        static int professorid;
        Professor()
        {
            this->cur_id = professorid;
            professorid++;
        }
        void getdata()
        {
            cin >> this->name >> this->age >> this->publications; 
        }
        void putdata()
        {
            cout << this->name << ' ' << this->age << ' ' << this->publications << ' ' << this->cur_id << endl;
        } 
    private :
        int publications;
        int cur_id;
};

class Student : public Person{
   
    public :
        static int studentid;
        Student()
        {
            this->cur_id = studentid;
            studentid++;
        }
        void getdata()
        {
            cin >> this->name >> this->age;
            for (int i = 0; i < 6; i++)
                cin >> this->marks[i];
        }
        void putdata()
        {
            int sum = 0;
            for (int i = 0; i < 6 ; i++)
                sum += this->marks[i];
            cout << this->name << ' ' << this->age << ' ' << sum << ' ' << this->cur_id << endl;
        }
    private :
        int marks[6];
        int cur_id;
};
int Professor::professorid = 1;
int Student::studentid = 1;
