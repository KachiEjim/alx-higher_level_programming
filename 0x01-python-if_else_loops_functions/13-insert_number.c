#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: list head
 * @number: number to store in the new node
 * Return: pointer to the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
        listint_t *temp, *new;


        new = malloc(sizeof(listint_t));
        if (new == NULL)
                return (NULL);
        new->n = number;

        if (*head == NULL || (*head)->n > number)
        {
                new->next = *head;
                *head = new;
                return (new);
        }
        temp = (*head)->next;
        while (temp != NULL)
        {
                if ((temp)->n >= number)
                {
                        new->next = temp;
                        temp = new;
                        return (new);
                }
                temp = temp->next;
        }

        new->next = NULL;
        temp->next = new;
        return (new);
}