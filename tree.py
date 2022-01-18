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
            
    def findVal(self, data):
        if data < self.data:
            if self.left is None:
                return( str(data) + " not found ")
            return self.left.findVal(data)
        elif data > self.data:
            if self.right is None:
                return( str(data) + " not found ")
            return self.right.findVal(data)
        else:
            print(str(self.data) + " is found")

myTree = Node(7) # create root

myTree.insert(15) # insert
myTree.insert(5)
myTree.insert(82)
myTree.insert(2.4)
myTree.printTree() # print
