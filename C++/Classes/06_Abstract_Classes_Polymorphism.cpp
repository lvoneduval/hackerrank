class LRUCache: public Cache{
    public :
        LRUCache(){}
        LRUCache(int cp)
        {
            this->cp = cp;
            tail = 0;
            head = 0;
        }
        void set(int key, int value)
        {
            Node *tmp;
            auto it = mp.find(key);
            
            if(it == mp.end()) 
            {
                tmp = new Node(0,this->head,key,value);
                this->mp[key] = tmp;
                if (this->head)
                    this->head->prev = tmp;
                this->head = tmp;
                if (mp.size() > this->cp)
                {
                    this->tail = this->tail->prev;
                    mp.erase(this->tail->next->key);
                    delete this->tail->next;
                    this->tail->next = 0;
                }
                if (!this->tail)
                    this->tail = tmp;
            }
            else
            {
                tmp = it->second;
                tmp->value = value;
                if (tmp->next)
                    tmp->next->prev = tmp->prev;
                if (tmp->prev)
                    tmp->prev->next = tmp->next;
                tmp->prev = 0;
                if (tmp != this->head)
                {
                    this->head->prev = tmp;
                    this->head = tmp;
                }
            }    
        }
        int get(int key)
        {
            Node *tmp;
            auto it = mp.find(key);
            if(it != mp.end())
                return it->second->value;
            return(-1); 
        }
        void printdl(Node *l,int sens)
        {
            Node *tmp = l;
            if (sens == 0)
            {
                while(tmp)
                {
                    if (tmp->prev)
                        printf("[%p %d %d]",tmp->prev, tmp->prev->key, tmp->prev->value);
                    else
                        printf("[0]");
                    printf("  %p %d %d   ",tmp, tmp->key, tmp->value);
                    if (tmp->next)
                        printf("[%p %d %d]\n",tmp->next, tmp->next->key, tmp->next->value);
                    else
                        printf("[0]\n");
                    tmp = tmp->next;
                }
            }
            else
            {
                while(tmp)
                {
                    if (tmp->prev)
                        printf("[%p %d %d]",tmp->prev, tmp->prev->key, tmp->prev->value);
                    else
                        printf("[0]");
                    printf("  %p %d %d   ",tmp, tmp->key, tmp->value);
                    if (tmp->next)
                        printf("[%p %d %d]\n",tmp->next, tmp->next->key, tmp->next->value);
                    else
                        printf("[0]\n");
                    tmp = tmp->prev;
                }
            }
        }
        void print(void)
        {
            printf("cp:%d size:%lu\nHead: %p %d %d\n",this->cp, this->mp.size(), this->head, this->head->key, this->head->value);
            printdl(this->head,0);
            printf("Tail: %p %d %d\n", this->tail, this->tail->key, this->tail->value);
            printdl(this->tail,1);
        }
};
