#include "lists.h"



/**
 * is_palindrome - checks if a linked list is a palindrome
 *
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, otherwise 0
 *
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *temp, *mid;

	slow = fast = temp = *head;
	mid = NULL;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			mid = slow->next;
			break;
		}
		if (!fast->next)
		{
			mid = slow->next->next;
			break;
		}
		slow = slow->next;
	}
	reverse(&mid);

	while (mid && temp)
	{
		if (temp->n !=  mid->n)
		{
			return (0);
		}
		mid = mid->next;
		temp = temp->next;
	}

	return (1);
}

/**
 * reverse- reverses a linked list
 *
 * @mid: pointer to the first node in the list
 *
 * Return: pointer to the first node in the new list
 *
 */

void reverse(listint_t **mid)
{
	listint_t *prev = NULL, *current = *mid, *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*mid = prev;

}
