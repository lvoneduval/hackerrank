#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
char *moove[4] = {"DOWN","UP","RIGHT","LEFT"};

typedef struct s_stat t_stat;
typedef struct s_list t_list;
struct  s_list{
	t_stat *data;
	t_list *next;
};         

struct s_stat{
	int           posx;
	int           posy;
	int           **tab;
	int           f;
	int           g;
	int           h;
	t_list        *nei;
	struct s_stat *prev;
	char          *moove;
};

t_stat *new_stat(int **tab,int x,int y, char *moove)
{
	t_stat *res;
	res = malloc(sizeof(t_stat));
	res->posx = x;
	res->posy = y;
	res->tab = tab;
	res->f = 0;
	res->g = 0;
	res->h = 0;
	res->nei = 0;
	res->prev = 0;
	res->moove = moove;
	return (res);
}

void copytab(int ***dst,int **src,int k)
{
	*dst = (int **)malloc(k * sizeof(int *));
	int  **tab = *dst;
	for (int i = 0; i < k; i++)
	{
		tab[i] = (int *)malloc(k * sizeof(int));
		for (int j = 0; j < k; j++)
			tab[i][j] = src[i][j];
	}
}

t_list *new_list(t_stat *data)
{
	t_list *res;
	res = malloc(sizeof(t_list));
	res->next = 0;
	res->data = data;
	return(res);
}

void addlst(t_list **l,t_list *new)
{
	if (!*l)
		*l = new;
	else
	{
		new->next = *l;
		*l = new;
	}
}

void addNei(t_stat *stat,int k)
{
	int x,y;
	int **tab;
	t_stat *tmp;
	x = stat->posx;
	y = stat->posy;
	if (x < k - 1)
	{
		copytab(&tab,stat->tab,k);
		tab[x][y] = tab[x + 1][y];
		tab[x + 1][y] = 0;
		tmp = new_stat(tab, x + 1, y, moove[0]);
		addlst(&(stat->nei), new_list(tmp));
	}
	if (x > 0)
	{
		copytab(&tab,stat->tab,k);
		tab[x][y] = tab[x - 1][y];
		tab[x - 1][y] = 0;
		tmp = new_stat(tab, x - 1, y, moove[1]);
		addlst(&(stat->nei), new_list(tmp));
	}
	if (y < k - 1)
	{
		copytab(&tab,stat->tab,k);
		tab[x][y] = tab[x][y + 1];
		tab[x][y + 1] = 0;
		tmp = new_stat(tab, x, y + 1, moove[2]);
		addlst(&(stat->nei), new_list(tmp));
	}
	if (y > 0)
	{
		copytab(&tab,stat->tab,k);
		tab[x][y] = tab[x][y - 1];
		tab[x][y - 1] = 0;
		tmp = new_stat(tab, x, y - 1, moove[3]);
		addlst(&(stat->nei), new_list(tmp));
	}
}

int manathanDis(t_stat *stat,int k)
{
	int **tab;
	int res;
	int tmp;

	tab = stat->tab;
	res =0;
	for (int i= 0; i < k;i++)
	{
		for (int j = 0; j< k ;j++)
		{
			tmp = tab[i][j];
			res += abs(i - tmp /3) + abs(j + tmp % 3);
		}
	}
	return(res);
}

int nbwrong(t_stat *stat, int k)
{
	int **tab;
	int res;

	tab = stat->tab;
	res =0;
	for (int i= 0; i < k;i++)
	{
		for (int j = 0; j< k ;j++)
		{
			res += (tab[i][j] != (i*k + j));
		}
	}
	return(res);
}

int heuristic(t_stat *stat,int k)
{
	return(manathanDis(stat,k) + nbwrong(stat,k) + stat->g);
}

int eg(int **t1,int **t2,int k)
{
	for (int i = 0; i < k;i++)
	{
		for (int j = 0; j < k; j++)
		{
			if (t1[i][j] != t2[i][j])
				return(0);
		}
	}
	return(1);
}

t_list *isin(t_stat *stat, t_list *l, int k)
{
	while (l)
	{
		if (eg(stat->tab,l->data->tab,k))
			return(l);
		l = l->next;
	}
	return(0);
}

void del(t_list **l,t_list *el)
{
	t_list *tmp1;
	t_list *tmp2;

	if (*l == el)
	{
		*l = (*l)->next;
	}
	else
	{
		tmp1 = *l;
		while(tmp1)
		{
			tmp2 = tmp1->next;
			if (tmp2 == el)
			{
				tmp1->next = tmp2->next;
				return;
			}
			tmp1 = tmp1->next;
		}
	}
}

void insertlst(t_list **l,t_list *l_el)
{
	t_list *tmp1;
	t_list *tmp2;

	t_stat *el;
	el = l_el->data;
	if(!*l)
	{
		*l = l_el;
		return ;
	}
	if ((*l)->data->f > el->f)
	{
		l_el->next = *l;
		*l = l_el;
	}
	else
	{
		tmp1 = *l;
		while(tmp1)
		{
			tmp2 = tmp1->next;
			if (!tmp2)
			{
				tmp1->next = l_el;
				return ;
			}
			if (tmp2->data->f > el->f)
			{
				tmp1->next = l_el;
				l_el->next = tmp2;
				return;
			}
			tmp1 = tmp1->next;
		}
	} 
}

t_stat *Astar(t_stat *end,t_stat *start,int k)
{
	t_list *openset;
	t_list *closset;
	t_list *tmp;
	t_list *lcur;
	t_stat *cur;
	t_list *tmpcur;
	t_list *tmp2;
	int tempg;
	int t;

	t = 0;
	closset = 0;
	tmp = 0;
	lcur = 0;
	cur = 0;
	tmpcur = 0;
	openset = new_list(start);
	while(openset)
	{
		lcur = openset;
		openset = openset->next;
		lcur->next = 0;
		cur = lcur->data;
		if (eg(cur->tab,end->tab,k))
			break;
		addlst(&closset,lcur);
		addNei(cur,k);
		tmp = cur->nei;
		tempg = cur->g + 1;
		while(tmp)
		{
			if ((tmpcur = isin(tmp->data,closset,k)))
			{
				if (tmpcur->data->g > tempg)
				{
					del(&closset,tmpcur);
					tmp->data->h = tmpcur->data->h;
					tmp->data->g = tempg;
					tmp->data->f = tmp->data->g + tmp->data->h;
					tmp->data->prev = cur;
					tmp2 = tmp->next;
					tmp->next = 0;
					insertlst(&openset,tmp);
					tmp = tmp2;
				}
				else
					tmp = tmp->next;
			}
			else if ((tmpcur = isin(tmp->data,openset,k)))
			{
				if (tmpcur->data->g > tempg)
				{
					del(&openset,tmpcur);
					tmp->data->h = tmpcur->data->h;
					tmp->data->g = tempg;
					tmp->data->f = tmp->data->g + tmp->data->h;
					tmp->data->prev = cur;
					tmp2 = tmp->next;
					tmp->next = 0;
					insertlst(&openset,tmp);
					tmp = tmp2;
				}
				else
					tmp = tmp->next;
			}
			else
			{
				tmp->data->h = heuristic(tmp->data,k);
				tmp->data->g = tempg;
				tmp->data->f = tmp->data->g + tmp->data->h;
				tmp->data->prev = cur;
				tmp2 = tmp->next;
				tmp->next = 0;
				insertlst(&openset,tmp);
				tmp = tmp2;
			}
		}
	}
	return (cur);
}



void printsol(t_stat *l)
{
	t_list *lst;

	lst = 0;
	int i;

	i = 0;
	while(l)
	{
		addlst(&lst,new_list(l));
		l = l->prev;
		i++;
	}
	printf("%d\n",i - 1);
	while (lst)
	{
		if(lst->data->moove)
			printf("%s\n",lst->data->moove);
		lst = lst->next;
	}
}

int main(void) {

	int k,tmp;
	int posx,posy;
	int **tab;
	int **final;
	t_stat *fin;
	t_stat *start;
	t_stat *won;

	scanf("%d",&k);
	tab = (int **)malloc(k * sizeof(int *));
	final = (int **)malloc(k * sizeof(int *));
	for (int i = 0; i < k; i++)
	{
		tab[i] = (int *)malloc(k * sizeof(int));
		final[i] = (int *)malloc(k * sizeof(int));
		for (int j = 0; j < k; j++)
		{
			scanf("%d",&tmp);
			tab[i][j] = tmp;
			final[i][j] = i * k + j;
			if (tmp == 0)
			{
				posx = i;
				posy = j;
			}
		}
	}
	won = new_stat(final,0, 0 ,0);
	start = new_stat(tab,posx , posy,0);
	fin = Astar(won,start,k);
	printsol(fin);
	return 0;
}
