class Node:
    def __init__ (self, data):
        self.right = None
        self.left = None
        self.data = data

    def insert(self, data):
        if self.data is None: # ! if there is no data in the root
            self.data = data # insert the data into the root
        else: # if there is data in the root
            if data < self.data: # ! if the data to be added is less than the current node
                if self.left is None: # ! if there is nothing in the left branch
                    self.left = Node(data) #insert data in the left branch
                else: #! if there is data in the left branch
                    self.left.insert(data) # recursively check the left branches until data can be added
            elif data > self.data: # ! if data to be inserted is greater than the current node
                if self.right is None: # ! if there is nothing in the right branch
                    self.right = Node(data) # insert data in the right branch
                else: # ! if there is data in the right branch
                    self.right.insert(data) # recursively check the right branches until data can be added
                
        def printTree(self):
        if self.left: # if there is something in the left branch
            self.left.printTree()
        print(self.data) # print root
        if self.right:# if there is something in the right branch
            self.right.printTree() 

root = Node('g')
root.insert('c')
root.insert('b')
root.insert('a')
root.insert('e')
root.insert('d')
root.insert('f')
root.insert('i')
root.insert('h')
root.insert('j')
root.insert('k')
