#include "lists.h"

/**
 * is_palindrome - a function that checks if a linkedlist is a palindrome
 * @head: pointer to the head of the list
 * Return: 0 if it's not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *secondHalf, *p1, *p2;

	if (head == NULL || (*head)->next == NULL)
		return (1);
	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	secondHalf = reverseList(&(slow->next));

	p1 = *head;
	p2 = secondHalf;

	while (p2 != NULL)
	{
		if (p1->n != p2->n)
			return (0);
	}

	return (1);
}

/**
 * reverseList - reverses a linkedlist
 * @head: pointer to the head of the list
 * Return: the reversed list
 */
listint_t *reverseList(listint_t **head)
{
	listint_t *prev = NULL, *curr = *head, *next = NULL;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	return (prev);
}
