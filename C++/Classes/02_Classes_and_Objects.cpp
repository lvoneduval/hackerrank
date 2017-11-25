// Write your Student class here
class Student{
  public:
    void input()
    {
        for (int i = 0; i < 5 ; i++)
            cin >> score[i];
    }
    int calculateTotalScore()
    {
        int sum;
        sum = 0;
        for(int i = 0 ; i < 5 ; i++)
            sum += score[i];
        return(sum);
    }
  private:
    int score[5];
};
