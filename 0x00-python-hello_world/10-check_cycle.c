#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * check_cycle - checks for a cyclr in a singly linked list
 * @list - The singly linked list to be checked
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *nodes[20] = {NULL},*current, *next;
	int i = 0, j;

	current = list;
	while (current != NULL)
	{
		nodes[i] = current;
		next = current->next;
		for (j = 0; nodes[j]; j++)
		{
			if (nodes[j] == next)
				return (1);
		}
		current = current->next;
		i++;
	}
	return (0);
}
