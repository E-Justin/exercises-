

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_nodes = 0

    def size(self):
        return self.num_nodes

    def enqueue(self, data):
        new_node = Node(data)
        current = self.head

        if self.head is None:  # if queue is emtpy
            # self.head = new_node
            # self.tail = new_node
            self.head = self.tail = new_node  # same as both statements above
        else:  # if queue is not empty
            self.tail.next = new_node  # place new_node after current tail
            self.tail = new_node  # set new_node to new tail node

        self.num_nodes += 1

    def dequeue(self):
        current_head = self.head  # get current head

        if current_head is None:  # if the list is empty
            return None

        self.head = current_head.next  # move head over 1
        self.num_nodes -= 1
        return current_head.data


q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')

print('Pass' if (q.size() == 3) else 'fail')
q.enqueue('d')
print('Pass' if (q.size() == 4) else 'fail')

print('Pass' if (q.dequeue() == 'a') else 'fail')
# print(q.dequeue())
print('Pass' if (q.dequeue() == 'd') else 'fail')
print('Pass' if (q.size() == 2) else 'fail')
