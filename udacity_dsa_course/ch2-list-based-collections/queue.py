class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        node = Node(data)
        if not self.head:
            self.head = self.tail = node
        else:
            last_node = self.tail
            last_node.next = node
            self.tail = last_node.next

    def dequeue(self):
        if not self.head:
            raise ValueError("Queue is empty.")
        elif not self.head.next:
            deleted_data = self.head.data
            self.head = self.tail = None
        else:
            deleted_data = self.head.data
            self.head = self.head.next
        return deleted_data

    def __repr__(self):
        print_str = "|Head| -> "
        node = self.head
        while node:
            print_str += str(node.data) + " -> "
            node = node.next
        return print_str + "|Tail|"


queue = Queue()
queue.enqueue(3)
print(queue)
queue.enqueue(6)
print(queue)
queue.enqueue(4)
print(queue)
print(queue.dequeue())
print(queue)
print(queue.dequeue())
print(queue)
print(queue.dequeue())
print(queue)
print(queue.dequeue())
print(queue)