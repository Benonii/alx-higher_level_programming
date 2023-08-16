#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - inserts a number in a SORTED linked list
 * @head: pointer to the beginning of the linked list
 * @number: The number to be inserted
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = NULL, *node = NULL, *next = NULL;

	current = *head;

	node = malloc(sizeof(listint_t));
	node->n = number;
	node->next = NULL;

	while (current != NULL)
	{
		next = current->next;
		if (next->n >= number)
		{
			node->next = current->next;
			current->next = node;
			break;
		}
		current = current->next;
	}
	return(node);
}
