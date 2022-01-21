class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None # set next to None (it does not exist yet)

class LinkedList:
    # constructor
    def __init__(self):
        self.head = Node() # create head Node
        
    # method to append a node to the list
    def append(self, data):
        newNode = Node(data) # create a new node with the given value
        currentNode = self.head # start at the front of the list
        while currentNode.next != None: # while the next node in line has a value
            currentNode = currentNode.next # move to the next node
        currentNode.next = newNode # place new node at the end of the list
        
    # method to get length of list
    def length(self):
        currentNode = self.head
        total = 0
        while currentNode.next != None:
            total += 1
            currentNode = currentNode.next
        return total
    
    # method to display list
    def display(self):
        listArr = [] # create empty array to hold each of the items in the list
        currentNode = self.head # start at the front of the list
        while currentNode.next != None: # while the next node has something in it
            currentNode = currentNode.next # move node over one
            listArr.append(currentNode.data) # append array with each item in the list
        print(listArr) # print list
            

List = LinkedList() # instantiate linked list
List.display() # display (nothing here yet)
List.append(12) # append 12
List.append(22) # append 22
List.display() # display list (12, 22)
print(List.length()) # print length
