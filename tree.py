class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
    
    #method to insert into tree
    def insert(self, data):
        if self.data is None:
            self.data = data
        else: # if there is data in the tree
            if data < self.data: # if the data to be inserted is less than the current node
                if self.left is None: # if there is nothing in the left branch
                    self.left = Node(data) # insert into left branch
                else: # if there is data in the left branch
                    self.left.insert(data) # recursively check left branch until data can be added
            elif data > self.data: # if the data to be inserted is greater than the current node
                if self.right is None: # if there is nothing in the right branch
                    self.right = Node(data) # insert data into right branch
                else: # if there is data in the right branch
                    self.right.insert(data) # recursively check right branch until data can be added
                    
    # method to print tree
    def printTree(self):
        if self.left: # if there is a left branch
            self.left.printTree() # prints left branch
        print(self.data) # prints root
        if self.right: # if there is a right branch
            self.right.printTree() # prints right branch
    
    # method to return if a value was found in the tree or not and the index it was found    
    def findVal(self, data):
        if data < self.data: # if its value is less,
            if self.left is None: # if nothing is there
                print(str(data) + " : NOT HERE ")
            else: # if there is data in the left branches
                return (self.left.findVal(data)) # recursively check the left branches
        elif data > self.data: # if its value is greater than
            if self.right is None: # if there is nothing there
                print(str(data) + " : NOT HERE ")
            else: # if there is data in the right branches
                return self.right.findVal(data) # recursively check right branches
        else:
            print(str(data) + " : FOUND IT ")
    
    def height(self, h = 0):
        """ Height = how many levels there are from the root to the lowest leaf """
        leftHeight = self.left.height(h + 1) if self.left else h
        rightHeight = self.right.height(h + 1) if self.right else h
        return max(leftHeight, rightHeight)
    

myTree = Node(7) # create root

myTree.insert(15) # insert
myTree.insert(5)
myTree.insert(82)
myTree.insert(2.4)
myTree.printTree() # print
