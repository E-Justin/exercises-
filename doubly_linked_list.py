class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = DoubleNode(data)

        # if there is nothing in the list
        if self.head is None:
            self.head = new_node # set new node to head node
            self.tail = new_node # set new node to tail node (there is only one node in the list at this point)
            return

        # if there is data in the list
        new_node.prev = self.tail # (old tail) <-- (new_node / new tail)
        self.tail.next = new_node # (old tail) --> (new_node / new tail)
        self.tail = new_node # set new_node to new tail node

    def display(self):
        current = self.head
        list_arr = []
        while current is not None:
            list_arr.append(current.data) # append current data value to list
            current = current.next  # move to next node
        print(list_arr)  # print contents of linked list

myDlist = DoublyLinkedList()
myDlist.append('1st node')
myDlist.append('2nd node')

