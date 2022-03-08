class Queue:
    def __init__(self):
        """ This method takes in an item and inserts that item into the 0th index
            of the list that is representing the Queue 
            The runtime is 0(n) or linear time, becaues inserting into the 0th  index of 
            a list forces all the other items in the list to move one inded to the right. """
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        """ Returns and removes the front most item from the Queue, which is represented
            by the last itme in the list 
            Runtime is 0(1) or constant time, because indexing to the end of a list
            happens in constant time """
        if self.items: # if there is something in the items list
            return self.items.pop() # remove and return  last item
        else:
            return None

    def peek(self):
        """ Returns the last item in the list which represents the front-most item
            in the Queue 
            Runtime is 0(1) or constant time because we are just indexing to the last item 
            of the list and returning the value found there. """
        if self.items: # if there is something in the items list
            return self.items[-1] # return last item
        else:
            return None

    def size(self):
        """ Returns the size of the Queue, which is represented by the length
             of the list
             Runtime is 0(1), or constant time, because were only returning the length """
        return len(self.items)

    def is_Empty(self):
        """ Returns a boolean value expressing whether or not the list representing the 
            Queue is empty
            
            Runs in constant time"""
        return self.items == [] # returns boolean value: T if items is an empty list, F if not

myQ = Queue()
myQ.dequeue()
print(myQ.is_Empty())
myQ.enqueue('apple')
print(myQ.items)
myQ.enqueue('banana')
print(myQ.items)
print(myQ.peek())
myQ.dequeue()
print(myQ.items)
print(myQ.is_Empty())

