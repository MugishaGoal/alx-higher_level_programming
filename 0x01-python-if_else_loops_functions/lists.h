#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked lists
 * @n: integer
 * @next_node: Points to the next node
 *
 * Description: A singly linked list
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next_node;
}listint_z;
size_t print_listint(const listint_z *head);
listint_z *add_node(listint_z **head, const int n);
void free listint(listint_z *head);
listint_z *add_node(listint_z *head int x);

#endif /* LIST_H */
