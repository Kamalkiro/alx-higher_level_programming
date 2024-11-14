#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *temp;
	int i = 0;

	while(list != NULL)
	{
		temp = list;
		list = list->next;
		while(list != NULL && i < 100000)
		{
			if (temp == list)
			{
				return (1);
			}
			list = list->next;
			i++;
		}
	}
	return (0);
}