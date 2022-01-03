class linkedListNode:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode


# 1, 2, 3

node1 = linkedListNode("1") # initialize with value
node2 = linkedListNode("2") # initialize with value
node3 = linkedListNode("3") # initialize with value
node4 = linkedListNode("4") # initialize with value

node1.nextNode = node2 # set nextNode to point to the next node
node2.nextNode = node3 # set nextNode to point to the next node
node3.nextNode = node4 # set nextNode to point to the next node


currentNode = node1 # starting point at the beginning of the linked list

while True:
    print(currentNode.value , '->')
    currentNode = currentNode.nextNode # move to the next node
     
    if currentNode is None: # if the end of the list has been reached
        print ("None") 
        break # exit loop
    
