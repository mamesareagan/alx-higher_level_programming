#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *curr = *head;
	listint_t *current;
	if ((*head) == NULL || (*head)->next == NULL)
		return (1);
	curr = curr->next;
	current = *head;
	while (current->next != NULL)
		current = current->next;
	if (current->n == curr->n)
		return (0);
	return (1);
}
