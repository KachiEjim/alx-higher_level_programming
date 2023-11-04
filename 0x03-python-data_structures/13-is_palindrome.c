#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 *
 * @head: double pointer to the head of the singly linked list
 *
 * Return: 0 if not palindrome, 1 if palindrome
 *
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp;
		int *items;
		int len = 0, i;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		len++;
		temp = temp->next;
	}

	items = malloc(sizeof(int) * len);
	if (items == NULL)
	return (0);

	temp = *head;
	for (i = 0; temp; i++)
	{
		items[i] = temp->n;
		temp = temp->next;
	}
	temp = *head;

	for (i = 0; i < len; i++, len--)
	{
		if (items[len - 1] != items[i])
		{
			free(items);
			return (0);
		}
	temp = temp->next;
	}
	free(items);
	return (1);
}
