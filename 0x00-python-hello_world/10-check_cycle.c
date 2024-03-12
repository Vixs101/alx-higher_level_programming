#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: pointer to the head of the list
 * Return: returns 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	const listint_t *slow = list;
	const listint_t *fast = list->next;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
		{
			return (1);
		}

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
