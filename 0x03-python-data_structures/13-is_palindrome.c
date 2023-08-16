#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: points to the beginning of the list
 *
 * Return: 1 if its a palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = NULL;
	int i = 0, len = 0, node[20];

	current = *head;
	while (current != NULL)
	{
		node[i] = current->n;
		len++;
		current = current->next;
	}
	for (i = 0; node[i]; i++)
	{
		if ((node[i]) != (node[len - 1]))
			return (0);
	}

	return (1);
}
