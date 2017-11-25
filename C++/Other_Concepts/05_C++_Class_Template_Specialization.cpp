template <> 
struct Traits<Fruit>
{
    static string name(int index)
    {
        string names[3] = {"apple", "orange", "pear"};
        if (index >= 0 && index < 3)
            return(names[index]);
        else
            return("unknown");
    }
};
template <> 
struct Traits<Color>
{
    static string name(int index)
    {
        string names[3] = {"red", "green", "orange"};
        if (index >= 0 && index < 3)
            return(names[index]);
        else
            return("unknown");
     }
};
