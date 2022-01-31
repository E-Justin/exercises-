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
        current = self.head
        while current.next is not None:
            current = current.next
            if current.data == data:
                return (str(data) + " was found ")
        return (str(data) + " was NOT found ")


    def deleteNode(self, data):
        temp = self.head # store head node

        if temp is not None: # if head node is the value to be deleted
            if temp.data == data:
                self.head = temp.next
                temp = None
                return

        # search for the value to be deleted and keep track of the 
        # previous node as we need to change prev.next
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next

        # if the value to be deleted does not exist in the list
        if temp is None:
            return 
        
        #unlink the node from linked list
        prev.next = temp.next
        temp = None


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
