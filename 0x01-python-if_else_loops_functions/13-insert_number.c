#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Author - tazy-dev
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *tmp = *head;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (!(*head) || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (tmp->next && tmp->next->n < number)
	{
		tmp = tmp->next;
	}

	new->next = tmp->next;
	tmp->next = new;
	return (new);
}
