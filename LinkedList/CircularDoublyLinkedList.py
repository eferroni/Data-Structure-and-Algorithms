class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node == self.tail:
                break
            node = node.next

    def createCDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = node
        node.next = node
        self.head = node
        self.tail = node
        return "The CDLL has been created"

    def insertCDLL(self, value, location):
        node = Node(value)
        if self.head is None:
            node.next = node
            node.prev = node
            self.head = node
            self.tail = node
        else:
            if location == 0:
                node.prev = self.tail
                node.next = self.head
                self.head.prev = node
                self.tail.next = node
                self.head = node
            elif location == -1:
                node.next = self.head
                node.prev = self.tail
                self.tail.next = node
                self.head.prev = node
                self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = node
                node.prev = tempNode
                node.next = nextNode
                nextNode.prev = node
                if tempNode == self.tail:
                    self.tail = node


cdll = CircularDoublyLinkedList()
cdll.createCDLL(1)
print([node.value for node in cdll])
cdll.insertCDLL(3, -1)
cdll.insertCDLL(4, -1)
cdll.insertCDLL(0, 0)
cdll.insertCDLL(2, 2)
print([node.value for node in cdll])
