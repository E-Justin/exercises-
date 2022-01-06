class LinkedList:
    # constructor
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode


node1 = LinkedList("A")
node2 = LinkedList('B')
node3 = LinkedList('C')
node4 = LinkedList('D')
node5 = LinkedList('E')

# point nodes to the next node in the list
node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4
node4.nextNode = node5

# set current node
currentNode = node1

while True: # while something is there...
    print (currentNode.value, '->') # print the value of currentNode
    currentNode = currentNode.nextNode # move currentNode to the next position in the list
    if currentNode == None: # if it has reached the end of the list...
        print ("None") # print none (bc it doesnt point to anything)
        break # exit loop


