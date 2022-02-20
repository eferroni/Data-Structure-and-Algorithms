class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Queue:
    def __init__(self) -> None:
        self.LinkedList = LinkedList()

    def isEmpty(self):
        return self.LinkedList.head is None

    def enqueue(self, value):
        newNode = Node(value)
        if self.isEmpty():
            self.LinkedList.head = newNode
            self.LinkedList.tail = newNode
        else:
            self.LinkedList.tail.next = newNode
            self.LinkedList.tail = newNode

    def dequeue(self):
        if self.isEmpty():
            return "is empty"

        deleteNode = self.LinkedList.head
        self.LinkedList.head = self.LinkedList.head.next
        if self.LinkedList.head is None:
            self.LinkedList.tail = None
        return deleteNode

    def peek(self):
        if self.isEmpty():
            return "empty"
        return self.LinkedList.head

    def delete(self):
        self.LinkedList.head = None
        self.LinkedList.tail = None

    def __str__(self):
        values = [str(x) for x in self.LinkedList]
        return " -> ".join(values)


custQueue = Queue()
custQueue.enqueue(0)
custQueue.enqueue(1)
custQueue.enqueue(2)
custQueue.enqueue(3)
custQueue.enqueue(4)
# print(custQueue)
# print(custQueue.dequeue())
# print(custQueue.dequeue())
# print(custQueue)
# print(custQueue.peek())
