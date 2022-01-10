If we use a LinkedQueue for a RoundRobin implementation, there is unnecessary effort in the combination of a dequeue operation followed soon after by an enqueue of the same element. One node is removed from the list, with appropriate adjustments to the head of the list and the size decremented and then a new node
is created  to reinsert at the tail of the list  and the size is incremented. 


If using a circularly linked list, the effective transfer of an item  from the "head" of the list to the "tail" of the list can be accomplished by advancing a reference that marks the boundary of the queue

We now provide  an implementation of a CircularQueue class that supports the entire queue ADT, together with an additional method, rotate(), that moves the first element of the queue to the back.(A similar method is supported by the dequeue class of Pythons collections module)

With this operation, a round-robin schedule can be more efficiently be implemented by performing the following steps:

1. Service element Q.front()
2. Q.rotate()
