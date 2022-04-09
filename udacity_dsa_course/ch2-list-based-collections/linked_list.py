class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        data_node = Node(data)
        if not self.head:
            self.head = data_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = data_node

    def __repr__(self):
        print_str = "|Head| -> "
        node = self.head
        while node:
            print_str += str(node.data) + " -> "
            node = node.next
        return print_str + "|None|"


ll = LinkedList()
ll.append(2)
print(ll)
ll.append(3)
print(ll)
ll.append(6)
print(ll)
