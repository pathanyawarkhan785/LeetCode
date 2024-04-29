#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *next;
};

void printLinkedList(struct node *head)
{
    while (head != NULL)
    {
        printf("%d -> ", head->data);
        head = head->next;
    }
}

struct node *insertBegin(struct node *head, int data)
{
    struct node *insBeg = (struct node *)malloc(sizeof(struct node));
    // printf("enter data: ");
    // scanf("%d", &insBeg->data);
    insBeg->data = data;
    insBeg->next = head;
    return insBeg;
}

struct node *remElem(struct node *head, int remInd)
{

    int count = 1;
    while (count != remInd)
    {
        // printf("\n%d->\n", head->data);
        head = head->next;
        // printf("%d", count);
        count++;
    }

    head->data = head->next->data;
    head->next = head->next->next;

    // printf("%d", head->data);
}

int main()
{
    struct node *head = (struct node *)malloc(sizeof(struct node));
    struct node *second = (struct node *)malloc(sizeof(struct node));
    struct node *third = (struct node *)malloc(sizeof(struct node));
    struct node *fourth = (struct node *)malloc(sizeof(struct node));

    head->data = 2;
    head->next = second;

    second->data = 4;
    second->next = third;

    third->data = 6;
    third->next = fourth;

    fourth->data = 8;
    fourth->next = NULL;

    // head = insertBegin(head, 12);
    remElem(head, 2);
    printLinkedList(head);

    return 0;
}
