
class Box
{
    public:
        Box(void)
        {
            this->l = 0;
            this->b = 0;
            this->h = 0;
        }
        Box(int length, int breadth, int height)
        {
            this->l = length;
            this->b = breadth;
            this->h = height;
        }
        Box(const Box &a)
        {
            this->l = a.getLength();
            this->b = a.getBreadth();
            this->h = a.getHeight();
        }
        int getLength(void) const
        {
            return (this->l);
        }
        int getBreadth(void) const
        {
            return (this->b);
        }
        int getHeight(void) const
        {
            return (this->h);
        }
        long long CalculateVolume(void)
        {
            long long vol;
            vol = this->l;
            vol *= this->h;
            vol *= this->b;
            return(vol);
        }
    bool operator<(const Box &a)
    {
        int le , be, he;
        le = a.getLength();
        be = a.getBreadth();
        he = a.getHeight();
        return (this->l < le || (this->l == le && (this->b < be || (this->b == be && this->h < he))));
    }
    

    private:
        int l;
        int b;
        int h;
};
ostream& operator<<(ostream& out, const Box& B)
{
        out << B.getLength() << " " << B.getBreadth() << " " << B.getHeight(); 
        return out;
}

//Implement the class Box  
//l,b,h are integers representing the dimensions of the box

// The class should have the following functions : 

// Constructors: 
// Box();
// Box(int,int,int);
// Box(Box);


// int getLength(); // Return box's length
// int getBreadth (); // Return box's breadth
// int getHeight ();  //Return box's height
// long long CalculateVolume(); // Return the volume of the box

//Overload operator < as specified
//bool operator<(Box& b)

//Overload operator << as specified
//ostream& operator<<(ostream& out, Box& B)
