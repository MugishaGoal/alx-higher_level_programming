#include <stddef.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *current;
    int values[2048];
    int i, size;

    if (*head == NULL)
        return (1);

    current = *head;
    size = 0;

    while (current)
    {
        values[size] = current->n;
        current = current->next;
        size++;
    }

    for (i = 0; i < size / 2; i++)
    {
        if (values[i] != values[size - 1 - i])
            return (0);
    }

    return (1);
}
