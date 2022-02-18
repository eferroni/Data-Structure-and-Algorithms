class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return " -> ".join(values)


class Stack:
    def __init__(self) -> None:
        self.LinkedList = LinkedList()

    def isEmpty(self):
        return self.LinkedList.head == None

    def minimum(self):
        if self.LinkedList.head is None:
            return "empty stack"
        min_value = self.LinkedList.head.value
        node = self.LinkedList.head
        while node:
            if node.value < min_value:
                min_value = node.value
            node = node.next
        return min_value

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if not self.isEmpty():
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.LinkedList.head.value
        else:
            return None

    def delete(self):
        self.LinkedList.head = None


customStack = Stack()
customStack.push(5)
customStack.push(1)
customStack.push(3)
print(customStack.LinkedList)
print(customStack.peek())
print(customStack.minimum())
