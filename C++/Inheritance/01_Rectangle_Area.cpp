
/*
 * Create classes Rectangle and RectangleArea
 */
class Rectangle
{
    public:
        void display()
        {
           cout << this->width << ' ' << this->height << endl; 
        }
    protected:
        int width;
        int height;
};

class RectangleArea: public Rectangle
{
    public:
        void read_input()
        {
            cin >> this->width;
            cin >> this->height;
        }
        void display()
        {
           cout << this->width * this->height << endl; 
        }
};
