class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created"

    def insertCSSL(self, value, location):
        node = Node(value)
        if self.head is None:
            node.next = node
            self.head = node
            self.tail = node
        else:
            if location == 0:
                node.next = self.head
                self.head = node
                self.tail.next = node
            elif location == -1:
                node.next = self.tail.next
                self.tail.next = node
                self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = node
                node.next = nextNode
                if tempNode == self.tail:
                    self.tail = node

    def traverseCSLL(self):
        if self.head is None:
            print("not exist")
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next
                if node == self.head:
                    break

    def searchCSLL(self, value):
        if self.head is None:
            return "not exist"
        else:
            node = self.head
            while node:
                if node.value == value:
                    return "founded"
                if node == self.tail:
                    return "not found"
                node = node.next

    def deleteCSLL(self, location):
        if self.head is None:
            return "empty singly list"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.head
                    while tempNode is not None:
                        if tempNode.next == self.tail:
                            break
                        tempNode = tempNode.next
                    tempNode.next = self.head
                    self.tail = tempNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                    if tempNode is None:
                        return False
                if tempNode.next is None:
                    return False
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                if tempNode.next is None:
                    self.tail = tempNode

    def deleteEntireCSLL(self):
        if self.head is None:
            return "empty singly list"
        else:
            self.head = None
            self.tail.next = None
            self.tail = None


# csll = CircularSinglyLinkedList()
# csll.createCSLL(1)
# print([node.value for node in csll])
csll = CircularSinglyLinkedList()
csll.insertCSSL(1, -1)
csll.insertCSSL(3, -1)
csll.insertCSSL(4, -1)
csll.insertCSSL(0, 0)
csll.insertCSSL(2, 2)
print([node.value for node in csll])
# csll.traverseCSLL()
# print(csll.searchCSLL(0))
# print(csll.searchCSLL(1))
# print(csll.searchCSLL(2))
# print(csll.searchCSLL(3))
# print(csll.searchCSLL(4))
# print(csll.searchCSLL(5))
csll.deleteCSLL(1)
print([node.value for node in csll])
csll.deleteEntireCSLL()
print([node.value for node in csll])
