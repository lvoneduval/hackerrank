//Overload operators + and << for the class complex
//+ should add two complex numbers as (a+ib) + (c+id) = (a+c) + i(b+d)
//<< should print a complex number in the format "a+ib"
Complex operator +(const Complex &a, const Complex &b)
{
    Complex c;
    c.a = a.a + b.a;
    c.b = a.b + b.b;
    return c;
}

ostream& operator <<(ostream& os, const Complex &b)
{
    os << b.a;
    if (b.b > 0)
        os<<"+i"<<b.b;
    else if (b.b < 0)
        os<<"-i"<<b.b;
    return(os);
}
