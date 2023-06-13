#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	current = *head;
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return new_node;
	}
	while (current->next != NULL && current->next->n < number)
	{
		current = current-> next;
	}
	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}
