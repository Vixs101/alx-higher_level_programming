#include "lists.h"

/**
 * insert_node - inserts a number into a sorted linked list
 * @head: pointer to the head of the list
 * @number: the number to be inserted in the list
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current = *head;
	listint_t *previous = NULL;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
		*head = new_node;
	else
	{
		while (current != NULL && current->n < number)
		{
			previous = current;
			current = current->next;
		}
		if (previous == NULL)
		{
			new_node->next = current;
			*head = new_node;
		}
		else
		{
			previous->next = new_node;
			new_node->next = current;
		}
	}
	return (new_node);
}
