class Deque:
    def __init__(self):
        self.items = []
    
    def addFront(self, item):
        """ Takes an item as a parameter and inserts it into the 0th index of 
            the list that is representing the Deque. 

            Runtime is 0(n) or linear, because every time you insert into the front of
            the list, all the other items in teh list need to shift one position
            to the right"""
        self.items.insert(0, item)

    def addRear(self, item):
        """ Takes in an item as a parameter and appends that item to the end of the 
            list that is representing the Deque.
            
            The runetime is constant because appending to the end of a list happens
            in constant time """
        self.items.append(item)
    
    def removeFront(self):
        """ Removes and returns the item in the 0th index of the list, which
            represents the front of the Deque.
            
            The runtime is linear, or 0(n), because when we remove an item from the 0th
            inex, all other items have to shift one index to the left."""
        if self.items: # if there are items in the list
            return self.items.pop(0) # remove first item
        else:
            return None

    def removeRear(self):
        """ Removes and returns the item in the last item of the  list, whcih represents
            the rear of the Deque.
            
            The runtime si constant because all we are doing is indexing to the end 
            of a list"""
        if self.items: # if there are items in the list
            return self.items.pop() # remove last item
        else:
            return None

    def peekFront(self):
        """ Returns the value found at the 0th index of the list, which representes
            the front of the deque

            The runtime is constant because all we are doing is indexing into
             a list."""
        if self.items:
            return self.items[0]
        else:
            return None

    def peekRear(self):
        """ Returns the value found at the -1st, or last index
        
            The runtime is constant because all we are doing is indexing into a list """
        if self.items:
            return self.items[-1]
        else:
            return None

    def size(self):
        """ Returns the length of the list, whcih is representing the Deque.
        
            The runtime will be constant because all we are doing is finding the length
            of a list and returning that value"""
        return len(self.items)

    def isEmpty(self):
        """ Checks to see if the list representing out Deque is empty. Returns True
            if if is, or False if it isnt
            
            Runtime is constant because all we are doing is checking to see if empty"""
        return self.items == []

myD = Deque()

print(myD.items)
print(myD.isEmpty())
myD.addFront('apple')
myD.addFront('banana')
myD.addRear('carrot')
print(myD.items)
print(myD.size())
print(myD.peekRear())
myD.removeRear()
print(myD.items)
print(myD.peekFront())
myD.removeFront()
print(myD.items)
print(myD.isEmpty())
