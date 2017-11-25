/*Write the class AddElements here*/
template <typename ELEM>
class AddElements{
    private:
        ELEM e;
    public:
        AddElements(ELEM ne)
        {
            this->e = ne;
        }
        ELEM add(ELEM to_add)
        {
            return(this->e + to_add);
        }
        ELEM concatenate(ELEM to_add)
        {
            return(this->add(to_add));
        }
};
