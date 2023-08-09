#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct new_listint_s
 * @n: integer
 * @next_node: points to the next node
 *
 * Description: Singly linked list
 */
typedef struct new_listint_s
{
	int n;
	struct new_listint_s *next_node;
}new_listint_z
size_t print_listint(const listint_z *head);
listint_t *add_node(listint_z **head, const int n);
void free_listint(listint_z *head);
int inspect_repetition(listint_z *list;

#endif /* LISTS_H */
