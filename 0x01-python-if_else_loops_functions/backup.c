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

                        if (previous == NULL)
                        {
                                new_node->next = *head;
                                *head = new_node;
                        }
                        else
                        {
                                previous->next = new_node;
                                new_node->next = current;
                        }
                }
        }
        return (new_node);
}

