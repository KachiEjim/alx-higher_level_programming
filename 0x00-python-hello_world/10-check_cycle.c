#include "lists.h"

/**
 * check_cycle - checks if a listint has a cycle
 *
 * @list: pointer listint element
 *
 * Return: returns 1 if a cycle is found and
 * zero otherwise
 *
 */

int check_cycle(listint_t *list)
{
	listint_t *temp, *check;

	if (list == NULL || list->next == NULL)
		return (0);
	check = list;
	temp = list->next;
	while (check && temp->next && temp->next->next)
	{
		if (check == temp)
			return (1);
		check = check->next;
		temp = temp->next->next;
	}
	return (0);
}
