#include <iostream>
#include <sstream>
using namespace std;

/*
Enter code for class Student here.
Read statement for specification.
*/

class Student{
  public:
    void set_age(int age)
    {
        this->age = age;
    }
    void set_standard(int i)
    {
        this->standard = i;
    }
    void set_first_name(string name)
    {
        this->first_name = name;
    }
    void set_last_name(string name)
    {
        this->last_name = name;
    }
    int get_age()
    {
       return(this->age); 
    }
    int get_standard()
    {
       return(this->standard); 
    }
    string get_first_name()
    {
       return(this->first_name); 
    }
    string get_last_name()
    {
       return(this->last_name); 
    }
    string to_string()
    {
        stringstream ss;
        char c = ',';
        ss << this->age << c << this->first_name << c << this->last_name << c << this->standard;
        return(ss.str());
    }
  private:
    int age;
    int standard;
    string first_name;
    string last_name;
};

int main() {
    int age, standard;
    string first_name, last_name;
    
    cin >> age >> first_name >> last_name >> standard;
    
    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);
    
    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    cout << st.to_string();
    
    return 0;
}
