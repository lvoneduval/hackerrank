void Print(Node *head)
{
  while (head)
  {
    printf("%d\n",head->data);
    head = head->next;
  }
  // This is a "method-only" submission. 
  // You only need to complete this method. 
}
