class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Dequeue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = self.tail = node
        else:
            last_node = self.tail
            last_node.next = node
            self.tail = last_node.next

    def append_left(self, data):
        node = Node(data)
        if not self.head:
            self.head = self.tail = node
        else:
            first_node = self.head
            node.next = first_node
            self.head = node

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


dequeue = Dequeue()
dequeue.append(3)
print(dequeue)
dequeue.append(6)
print(dequeue)
dequeue.append(4)
print(dequeue)
dequeue.append_left(30)
print(dequeue)
dequeue.append_left(60)
print(dequeue)
dequeue.append_left(40)
print(dequeue)