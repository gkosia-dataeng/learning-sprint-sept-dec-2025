'''Fast and slow pointers is used to detect cycles in lists 
    Detect if a list has a cycle


    Fast pointer movess 2 at a time
    Slow pointer moves 1 at a time

    If Fast reach the endo of the list there is no cycle


    If i detect a point in cycle (fast and slow pointer met), to detect the start of the cycle i am reseting the slow to start of ht elist and move them both by 1
    Where they will meet again is the start of the cycle
'''


#Define the Linked list

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

#Define the nodes
head = LinkedListNode(1)
b_node = LinkedListNode(2)
c_node = LinkedListNode(3)
d_node = LinkedListNode(4)

# Define the edges
head.next = b_node
b_node.next = c_node
c_node.next = d_node
d_node.next = c_node



def has_cycle(head):
    slow = head
    fast = (head.next)

    while fast and fast.next:

        if slow == fast:
            return True
        
        slow = slow.next
        fast = fast.next.next
    return False

print(has_cycle(head))