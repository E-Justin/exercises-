class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = Node()
    
    def append(self, data):
        current = self.head 
        newNode = Node(data)
        while current.next is not None:
            current = current.next
        current.next = newNode
    
    def length(self):
        current = self.head
        total = 0
        while current.next is not None:
            current = current.next
            total += 1
        return total

    def display(self):
        current = self.head
        listArr = []
        while current.next is not None:
            current = current.next
            listArr.append(current.data)
        print(listArr)
    
    def findVal(self, data):
        current = self.head # start at front of list
        while current.next is not None: # while there is something there
            current = current.next # move to next position
            if current.data == data: # if we found the value we are looking for
                return (str(data) + " was found ") # return that we found it
        return (str(data) + " was NOT found ") # else: not found


   def deleteNode1(self, data):
        current = self.head
        
        # if the head node is the one to be deleted
        if current is not None:
            if current.data == data:
                self.head = current.next
                current = None
                return 
        
        # if the node to be deleted is in the middle somewhere
        prev = None
        while current is not None:
            if current.data == data: # search through until value to be deleted is found
                break
            prev = current
            current = current.next

        # if there is nothing in the list/ if value is not in the list and current is pointing to None        
        if current is None:
            return None

        prev.next = current.next
        current = None


List = LinkedList()
List.append(17)
List.append(5)
List.append(16)
List.append(7)
print(List.findVal(17))
print(List.findVal(5))

List.display()
print(List.length())

List.deleteNode(5)
List.display()
print(List.length())
print(List.findVal(5))