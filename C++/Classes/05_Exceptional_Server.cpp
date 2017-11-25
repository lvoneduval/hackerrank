        try 
        {
            int comp = Server::compute(A,B);
            cout << comp << endl;
        }
        catch (bad_alloc& e)
        {
           cout << "Not enough memory" <<endl; 
        }
        catch (exception &e)
        {
            cout << "Exception: " << e.what() << endl;
        }
        catch (...)
        {
           cout << "Other Exception" << endl;
        }
