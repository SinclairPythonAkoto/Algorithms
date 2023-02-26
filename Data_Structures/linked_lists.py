"""Linked Lists

A linked list is a collection of nodes, where each node contains a value and a 
reference to the next node in the list. Unlike arrays, linked lists do not provide 
random access to their elements, meaning that elements must be accessed sequentially. 
Linked lists are useful for applications where elements are frequently inserted or deleted, 
as these operations can be performed efficiently by adjusting the references between nodes.

Linked lists are used in a variety of real-world applications, including operating systems, 
file systems, and database management systems. For example, in a file system, a linked list 
can be used to represent the blocks that make up a file. Each block can be represented as a 
node in the list, with a reference to the next block in the file. When a file is read or 
written, the operating system can traverse the linked list to access the blocks in the correct 
order. Linked lists are also used in database management systems to represent the rows in a 
table. Each row can be represented as a node in the list, with a reference to the next row. 
When queries are executed on the table, the database management system can traverse the 
linked list to retrieve the relevant rows.
"""
# define a node for the linked list
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


# define linked list class
class LinkedList:
    def __init__(self) -> None:
        self.head = None

    # add new node to beginning of list
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    # remove first node with given value
    def remove(self, value):
        if self.head is None:
            return
        
        if self.head.value == value:
            self.head = self.head.next
            return
        
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
    
    # print the list
    def print(self):
        curent_node = self.head
        while curent_node is not None:
            print(curent_node.value)
            curent_node = curent_node.next


# create a linked list and some nodes
new_list: LinkedList = LinkedList()
new_list.prepend(3)
new_list.prepend(2)
new_list.prepend(1)

new_list.print()

new_list.remove(2)

new_list.print()

# can find the value of the next node. 
# If at the end, it will return to beginning
print(new_list.head.next.value)

# Output
# 1
# 2
# 3
# 1
# 3
# 3