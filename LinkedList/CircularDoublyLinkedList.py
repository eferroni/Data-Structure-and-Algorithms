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

    def traverseCDLL(self):
        if self.head is None:
            print("not exist")
        else:
            node = self.head
            while node:
                print(node.value)
                if node == self.tail:
                    break
                node = node.next

    def reverseTraverseCDLL(self):
        if self.head is None:
            print("not exist")
        else:
            node = self.tail
            while node is not None:
                print(node.value)
                if node == self.head:
                    break
                node = node.prev

    def searchCDLL(self, value):
        if self.head is None:
            return "not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == value:
                    return f"{value}: founded"
                if node == self.tail:
                    break
                node = node.next
            return f"{value}: not found"

    def deleteCDLL(self, location):
        if self.head is None:
            return "empty singly list"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head

            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
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
                deleteNode = tempNode.next
                nextNode = deleteNode.next
                tempNode.next = nextNode
                nextNode.prev = tempNode
                if tempNode.next is None:
                    self.tail = tempNode

    def deleteEntireCDLL(self):
        if self.head is None:
            return "empty singly list"
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None


cdll = CircularDoublyLinkedList()
cdll.createCDLL(1)
print([node.value for node in cdll])
cdll.insertCDLL(3, -1)
cdll.insertCDLL(4, -1)
cdll.insertCDLL(0, 0)
cdll.insertCDLL(2, 2)
print([node.value for node in cdll])
# cdll.traverseCDLL()
# print()
# cdll.reverseTraverseCDLL()
print(cdll.searchCDLL(3))
print(cdll.searchCDLL(5))
cdll.deleteCDLL(1)
print([node.value for node in cdll])
cdll.deleteEntireCDLL()
print([node.value for node in cdll])
