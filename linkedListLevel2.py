class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = Node()
    
    def append(self, data):
        current = self.head # start at front
        newNode = Node(data) # create newNode to add the data to the list
        while current.next is not None: # while the end of the list has not been reached
            current = current.next # move to the next position
        current.next = newNode # when the end of the list has been reached, insert the newNode
    
    def length(self):
        current = self.head # start at the front
        total = 0 # set total to 0
        while current.next is not None: # whiel the end of the list has not been reached
            current = current.next # move to the next position
            total += 1 # add one to total
        return total

    def display(self):
        current = self.head # start at front
        listArr = [] # create an emtpy list to append data values to later
        while current.next is not None: # while the end of the list has not been reached
            current = current.next # move to the next position
            listArr.append(current.data) # append each data value, one at a time to the list
        print(listArr) # print the list with all values from linked list
    
    def findVal(self, data):
        current = self.head # start at front of list
        while current.next is not None: # while there is something there
            current = current.next # move to next position
            if current.data == data: # if we found the value we are looking for
                return (str(data) + " was found ") # return that we found it
        return (str(data) + " was NOT found ") # else: not found


   def deleteNode(self, data):
        current = self.head # start at head

        # if the head node is the one to be deleted
        if current is not None: # if there is something there
            if current.data == data: # if value to be deleted has been found at the head node
                self.head = current.next # move head of the list over one
                current = None # delete node
                return None

        # if the node to be deleted is not the head node
        prev = None
        while current is not None: # while the end of the list has not been reached
            if current.data == data: # if the value to be deleted has been found
                break
            prev = current #  prev holds current's previous place
            current = current.next # move to next node

        # if there is nothing in the list/ if the end of the list has been reached without finding the value to delete
        if current is None: 
            return None

        prev.next = current.next # skip over the node to be deleted
        current = None # set node to be deleted to None


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
