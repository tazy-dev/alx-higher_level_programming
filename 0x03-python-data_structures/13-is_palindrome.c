#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node in the list
 *
 * Return: pointer to the first node in the new list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}

	*head = prev;

	return (*head);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *first_half = *head, *scan = *head, *second_half = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		/*scan will iter the list twice fast as first_half*/
		/*this results in first half reaching the nmiddle of the list*/
		scan = scan->next->next;
		if (scan == NULL) /*if list length is even*/
		{
			/*second half start from the next element after first half*/
			second_half = first_half->next;
			break;
		}
		if (scan->next == NULL) /*if list length is odd*/
		{
			/*second half start from the element after the middle*/
			second_half = first_half->next->next; /*middle element not checked*/
			break;
		}
		first_half = first_half->next;
	}
	reverse_listint(&second_half);
	while (*head && second_half)
	{
		if ((*head)->n == second_half->n)
		{
			*head = (*head)->next;
			second_half = second_half->next;
		}
		else
			return (0);
	}
	return (1);
}

