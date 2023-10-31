#include "lists.h"
#include <stdio.h>
#include <stdlib.h>


/**
 * insert_node - inserts a number into a sorted singly linked list.
 *
 * @head: list head
 *
 * @number: number to store in the new node
 *
 * Return: pointer to the new node
 *
 */

listint_t *insert_node(listint_t **head, int number)
{
        listint_t *temp, *new;


        new = malloc(sizeof(listint_t));
        if (new == NULL)
                return (NULL);
        new->n = number;
        temp = *head;

        if (*head == NULL || (*head)->n > number)
        {
                new->next = *head;
                *head = new;
                return (new);
        }

        while (temp->next != NULL)
        {
                if ((temp->next)->n >= number)
                {
                        new->next = temp->next;
                        temp->next = new;
                        return (new);
                }
                temp = temp->next;
        }

        new->next = NULL;
        temp->next = new;
        return (new);
}