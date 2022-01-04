class LinkedListNode:
    def __init__ (self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode


#initialize nodes
node1 = LinkedListNode("1")
node2 = LinkedListNode("2")
node3 = LinkedListNode("3")
node4 = LinkedListNode("4")


node1.nextNode = node2 # link node 1 to node 2
node2.nextNode = node3 # link node 2 to node 3
node3.nextNode = node4 # link node 3 to node 4

currentNode = node1

while True:
    print(currentNode.value, "->")
    currentNode = currentNode.nextNode # move to next node
    if currentNode == None: # if it has reached the end of the list
        print("None") # it points to nothing
        break # exit loop



