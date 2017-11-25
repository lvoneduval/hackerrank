#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <limits.h>

typedef struct s_node {
	char **tab;
	int depth;
	int player;
	char v;
	int posx;
	int posy;
	int u;
	struct s_node **children;
	int nbchild;
}				t_node;

void	free_tab(char ***to_free);
void	free_node(t_node **to_free);
char	**copytab(char **tab);
t_node	*new_node(char **tab, int dep, int player, int posx, int posy);
t_node	**create_children(t_node *this);
t_node *max_turn(t_node *node, int alpha, int beta);
t_node *min_turn(t_node *node, int alpha, int beta);
void	minimax(char c, char tab[3][3]);
int		game_status(t_node *node);
int		main(void);
int 	max(int x, int y);
int 	min(int x, int y);

char *car = "XO";

int max(int x ,int y)
{
	return (x ^ ((x ^ y) & -(x < y)));
}

int min(int x, int y)
{
	return (y ^ ((x ^ y) & -(x < y)));
}

/**************************************** free functions ***********************************************/
																										//
// free a board																							//
void free_tab(char ***to_free)																			//
{																										//
	char **tmp;																							//
																										//
	tmp = *to_free;																						//
	for (int i = 0; i < 3; i++)																			//
		free( tmp[i] );																					//
																										//
	free( tmp );																						//
	*to_free = 0;																						//
}																										//
																										//
//free a node																							//
void free_node(t_node **to_free)																		//
{																										//
	t_node *tmp;																						//
																										//
	tmp = *to_free;																						//
	free_tab(&(tmp->tab));																				//
	for (int i = 0; i < tmp->nbchild; i++)																//
		free_node( &(tmp->children[i]) );																//
																										//
	free( tmp );																						//
	*to_free = 0;																						//
}																										//
/*******************************************************************************************************/



/************************************** create functions ***********************************************/
																										//
// copy board																							//
char **copytab(char **tab)																				//
{																										//
	char **cpy;																							//
																										//
	cpy = (char **)(malloc( sizeof(char *) * 3 ));														//
	for (int i = 0; i < 3; i++)																			//
	{																									//
		cpy[i] = (char *)malloc( sizeof(char) * 3 );													//
	}																									//
																										//
	for (int i = 0; i < 3; i++)																			//
	{																									//
		for (int j = 0; j < 3; j++)																		//
			cpy[i][j] = tab[i][j];																		//
	}																									//
	return (cpy);																						//
}																										//
																										//
// create a node																						//
t_node	*new_node(char **tab, int dep, int player, int posx, int posy)									//
{																										//
	t_node *res;																						//
																										//
	res = (t_node *)malloc(sizeof(t_node));																//
	res->tab = tab;																						//
	res->depth = dep;																					//
	res->player = player;																				//
	res->v = car[player];																				//
	res->posx = posx;																					//
	res->posy = posy;																					//
	res->children = 0;																					//
	res->nbchild = 0;																					//
	res->u = 0;																							//
	return(res);																						//
}																										//
																										//
// create all children of node																			//
t_node **create_children(t_node *this)																	//
{																										//
	int nb;																								//
	char **tmptab;																						//
	t_node **children;																					//
	nb = 0;																								//
	tmptab = this->tab;																					//
	for (int i = 0; i < 3; i++)																			//
		for (int j = 0; j < 3; j++)																		//
			if (tmptab[i][j] == '_')																	//
				++nb;																					//
	children = (t_node **)malloc(sizeof(t_node *) * nb);												//
	this->nbchild = nb;																					//
	nb = 0;																								//
	for (int i = 0; i < 3; i++)																			//
		for (int j = 0; j < 3; j++)																		//
			if (tmptab[i][j] == '_')																	//
			{																							//
				tmptab = copytab(this->tab);															//
				tmptab[i][j] = this->v;																	//
				children[nb] = new_node(tmptab, this->depth + 1, (this->player + 1) % 2, i, j);			//
				++nb;																					//
			}																							//
	return(children);																					//
}																										//
/*******************************************************************************************************/


/************************************** MiniMax functions **********************************************/
// max turn;																							//
t_node *max_turn(t_node *node, int alpha, int beta)														//
{																										//
	int end;																							//
	int nb;																								//
	int u;																								//
	int posx;																							//
	int posy;																							//
	t_node *tmp;																						//
	t_node *tmp2;																						//
																										//
	end = game_status(node);																			//
	if (end >= 0)																						//
	{																									//
		node->u = -end;																					//
		return (node);																					//
	}																									//
	u = INT_MIN;																						//
	node->children = create_children(node);																//
	nb = node->nbchild;																					//
	for (int i = 0; i < nb; i++)																		//
	{																									//
		tmp = node->children[i];																		//
		tmp2 = min_turn(tmp,alpha,beta);																//
		if (tmp2->u > u)																				//
		{																								//
			u = tmp2->u;																				//
			posx = tmp->posx;																			//
			posy = tmp->posy;																			//
		}																								//
		if (u >= beta)																					//
			break ;																						//
		alpha = max(alpha,u);																			//
	}																									//
	node->u = u;																						//
	if (node->depth == 0)																				//
	{																									//
		node->posx = posx;																				//
		node->posy = posy;																				//
	}																									//
	return(node);																						//
}																										//
																										//
// min turn;																							//
t_node *min_turn(t_node *node, int alpha, int beta)														//
{																										//
	int end;																							//
	int nb;																								//
	int u;																								//
	int posx;																							//
	int posy;																							//
	t_node *tmp;																						//
	t_node *tmp2;																						//
																										//
	end = game_status(node);																			//
	if (end >= 0)																						//
	{																									//
		node->u = end;																					//
		return (node);																					//
	}																									//
	u = INT_MAX;																						//
	node->children = create_children(node);																//
	nb = node->nbchild;																					//
	for (int i = 0; i < nb; i++)																		//
	{																									//
		tmp = node->children[i];																		//
		tmp2 = max_turn(tmp,alpha, beta);																//
		if (tmp2->u < u)																				//
		{																								//
			u = tmp2->u;																				//
			posx = tmp->posx;																			//
			posy = tmp->posy;																			//
		}																								//
		if(u <= alpha)																					//
			break ;																						//
		beta = min(beta,u);																				//
	}																									//
	node->u = u;																						//
	return(node);																						//
}																										//
// main minmax function																					//
void minimax(char c, char tab[3][3])																	//
{																										//
	int player;																							//
	t_node *init;																						//
	t_node *res;																						//
	char **cpy;																							//
																										//
	cpy = (char **)(malloc( sizeof(char *) * 3 ));														//
	for (int i = 0; i < 3; i++)																			//
	{																									//
		cpy[i] = (char *)malloc( sizeof(char) * 3 );													//
	}																									//
																										//
	for (int i = 0; i < 3; i++)																			//
	{																									//
		for (int j = 0; j < 3; j++)																		//
			cpy[i][j] = tab[i][j];																		//
	}																									//
	player = (c == 'X') ? 0 : 1;																		//
	init = new_node(cpy, 0, player, -1, -1);															//
	res = max_turn(init, INT_MIN, INT_MAX);																//
	printf("%d %d\n", res->posx, res->posy);															//
	free_node(&init);																					//
}																										//
/*******************************************************************************************************/


/************************************* tictactoe functions *********************************************/
																										//
// Status game function -1 isnt over, 0 Tie, 1 win														//
int game_status(t_node *node)																			//
{																										//
	static int l = 0;
	printf("%d\n",l);
	l++;
	int p;																								//
	char v = car[(node->player + 1) % 2];																//
	char **tab = node->tab;																				//
	int posx = node->posx;																				//
	int posy = node->posy;																				//
																										//
	if (posx == -1)																						//
		return(-1);																						//
																										//
	// check row																						//
	p = 0;																								//
	for (int i = 0; i < 3; i++)																			//
		if (tab[posx][i] == v)																			//
			p++;																						//
	if (p == 3)																							//
		return(1);																						//
																										//
	//check col																							//
	p = 0;																								//
	for (int i = 0; i < 3; i++)																			//
		if (tab[i][posy] == v)																			//
			p++;																						//
	if (p == 3)																							//
		return(1);																						//
																										//
	//check first diagonale																				//
	if (posx == posy)																					//
	{																									//
		p = 0;																							//
		for (int i = 0; i < 3; i++)																		//
			if (tab[i][i] == v)																			//
				p++;																					//
		if (p == 3)																						//
			return(1);																					//
	}																									//
																										//
	//check the second one																				//
	if (posx == 2 - posy)																				//
	{																									//
		p = 0;																							//
		for (int i = 0; i < 3; i++)																		//
			if (tab[i][2 - i] == v)																		//
				p++;																					//
		if (p == 3)																						//
			return(1);																					//
	}																									//
																										//
	//check Tie																							//
	for (int i = 0; i < 3; i++)																			//
		for (int j = 0; j < 3; j++)																		//
			if(tab[i][j] == '_')																		//
				return (-1);																			//
	return (0);																							//
}																										//
																										//
// main function																						//
int main(void) {																						//
	int i;																								//
	char player;																						//
	char board[3][3];																					//
																										//
	//If player is X, I'm the first player.																//
	//If player is O, I'm the second player.															//
	scanf("%c", &player);																				//
																										//
	//Read the board now. The board is a 3x3 array filled with X, O or _.								//
	for(i=0; i<3; i++) {																				//
		scanf("%s[^\n]%*c", board[i]);																	//
	}																									//
																										//
	minimax(player,board);																				//
	return 0;																							//
}																										//
/*******************************************************************************************************/
