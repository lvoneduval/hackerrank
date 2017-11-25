class BadLengthException{
    public :
        BadLengthException(void)
        {
            ;
        }
        BadLengthException(int n)
        {
            this->c = n;
        }
        int what(void)
        {
            return(this->c);
        }
    private :
    int c;
};
