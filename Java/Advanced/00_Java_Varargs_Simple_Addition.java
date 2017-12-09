class Add{
    void add(Integer ...inte)
    {
        int i = 0;
        int sum = 0;
        for (int n: inte)
        {
            sum += n;
            if (i != 0)
            {
                System.out.print("+");
            }
            i++;
            System.out.print(n);
        }
        System.out.format("=%d\n",sum);
    }
}
