class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    # constructor
    def __init__(self):
        self.head = Node()
    # method to append a node to the list
    def append(self, data):
        newNode = Node(data)
        currentNode = self.head
        while currentNode.next != None:
            currentNode = currentNode.next
        currentNode.next = newNode
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
        listArr = []
        currentNode = self.head
        while currentNode.next != None:
            currentNode = currentNode.next
            listArr.append(currentNode.data)
        print(listArr)
            

List = LinkedList() # instantiate linked list
List.display() # display (nothing here yet)
List.append(12) # append 12
List.append(22) # append 22
List.display() # display list (12, 22)
print(List.length()) # print length
