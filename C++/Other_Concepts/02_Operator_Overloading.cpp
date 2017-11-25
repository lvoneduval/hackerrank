class Matrix{
    public:
        vector<vector<int>> a;
        Matrix operator+(const Matrix &b)
        {
            Matrix res;
            int s1 = this->a.size();
            int s2 = b.a[0].size();
            for(int i = 0; i < s1; i++)
            {
                vector<int> d;
                for (int j = 0; j < s2 ; j++)
                {
                    d.push_back(this->a[i][j] + b.a[i][j]);
                }
                res.a.push_back(d);
            }
            return res;
        }
};
