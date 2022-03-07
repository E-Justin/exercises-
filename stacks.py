class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """ Accepts an item as a parameter and appends it to the end of the list 
            and returns nothing 
            The runtime for this method is 0(1), or constant time, because 
            appending to the end of a list happens in constant time"""
        self.items.append(item)

    def pop(self):
        """ removes and returns the last item from the list, which is also the top item 
            of the stack.
            The runtime is 0(1), or constant time, because all it does is index 
            to the last item of the list."""
        if self.items: # if the list is not empty
            return self.items.pop()
        else: # if the list is empty
            return None

    def peek(self):
        """ This method returns the last item in the list, which is also the item 
            at the top of the Stack
            This method runs in constant time because indexing into a list is done 
            in constant time."""
        if self.items: # if there is data in the list
            return self.items[-1] # return the last item in the list
        else:
            return None

    def size(self):
        """ THis method returns the length of the list 
            This method runs in constant time because finding the length of a list
            happens in constant time """
        return len(self.items)

    def is_empty(self):
        """ THis method returns a boolean value describig whether or not the 
        Stack is empty """
        return self.items == []

myStack = Stack()
print(myStack.is_empty())
print(myStack.size())
myStack.peek()
myStack.pop()
myStack.push('apple')
myStack.push('banana')
print(myStack.is_empty())
print(myStack.size())
print(myStack.items)
myStack.pop()
print(myStack.items)
print(myStack.peek())
