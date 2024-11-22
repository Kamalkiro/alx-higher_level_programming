#include "lists.h"
int check(listint_t **head, int a, int b);

int is_palindrome(listint_t **head)
{
	listint_t *lwla = NULL, *lkhra = NULL, *ras = *head;
	int i = 0, x = 0, chi = 0;
	
	if (!*head || !(*head)->next)
		return 1;
	while (ras)
	{
		i++;
		ras = ras->next;
	}
	while (x < i)
	{
		chi += check(head, x, i);
		x++;
	}
	if (chi == 0)
		return 1;
	else
		return 0;
}
int check(listint_t **head, int a, int b)
{
	listint_t *cu = *head, *nii = NULL;
	int x = 0;

	while (x < a && cu)
	{
		cu = cu->next;
		x++;
	}
	x = 1;
	nii = *head;
	while(x + 1 <= b - a && nii ->next)
	{
		nii = nii->next;
		x++;
	}
	if(nii->n == cu->n)
		return 0;
	else
	{
		return 1;
	}
}