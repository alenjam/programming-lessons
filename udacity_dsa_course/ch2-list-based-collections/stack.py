class Node:
    def __init__(self, data, next=None):
        self.data =  data
        self.next = next


class Stack:
    def __init__(self, head=None):
        self.head = head

    def push(self, data):
        node = Node(data)
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node

    def pop(self):
        current = self.head
        if not self.head:
            raise ValueError("Stack is empty")
        elif not self.head.next:
            deleted_node = self.head.data
            self.head = None
        else:
            while current.next.next:
                current = current.next
            else:
                deleted_node = current.next.data
                current.next = None
        return deleted_node

    def __repr__(self):
        print_str = "|Head| -> "
        node = self.head
        while node:
            print_str += str(node.data) + " -> "
            node = node.next
        return print_str + "|None|"


stack = Stack()
stack.push(3)
print(stack)
stack.push(6)
print(stack)
stack.push(4)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)