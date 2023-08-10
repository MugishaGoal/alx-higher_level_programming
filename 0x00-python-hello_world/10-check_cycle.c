#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle in it
* @list: a pointer to the head
* Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
    listint_t *slow = list;
    listint_t *speedy = list;

    while (speedy != NULL && speedy->next != NULL)
    {
        slow = slow->next;
        speedy = speedy->next->next;

        if (slow == speedy)
            return (1);
    }

    return (0);
}
