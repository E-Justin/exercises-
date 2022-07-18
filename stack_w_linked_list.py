class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.num_nodes = 0

    def push(self, data):
        new_node = Node(data)  # create new node
        current_head = self.head  # find current head node

        self.head = new_node  # set new node to head node

        if current_head is not None:  # if there is data in the list
            self.head.next = current_head  # move old head node to the second position

        self.num_nodes += 1  # increment total by 1

    def pop(self):
        # if the list is empty
        if self.head is None:
            return None
        # if list is not empty
        current = self.head  # find current node
        self.head = current.next  # move head node over by 1
        self.num_nodes -= 1  # decrement total by 1
        return current.data  # return the value popped off


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print('Pass' if (stack.num_nodes == 5) else 'Fail')
stack.push(5)

print('Pass' if (stack.num_nodes == 5) else 'Fail')
print('Pass' if (stack.pop() == 5) else 'Fail')
print('Pass' if (stack.pop() == 4) else 'Fail')
