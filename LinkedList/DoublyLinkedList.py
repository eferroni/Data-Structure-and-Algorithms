class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None


class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createDLL(self, value):
        newNode = Node(value)
        newNode.prev = None
        newNode.next = None
        self.head = newNode
        self.tail = newNode

    def insertDLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            newNode.prev = None
            newNode.next = None
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == -1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                newNode.prev = tempNode
                newNode.next = nextNode
                tempNode.next = newNode
                nextNode.prev = newNode
                if tempNode == self.tail:
                    self.tail = newNode

    def traverseDLL(self):
        if self.head is None:
            print("not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def reverseTraverseDLL(self):
        if self.head is None:
            print("not exist")
        else:
            node = self.tail
            while node is not None:
                print(node.value)
                node = node.prev

    def searchDLL(self, value):
        if self.head is None:
            return "not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == value:
                    return f"{value}: founded"
                node = node.next
            return f"{value}: not found"

    def deleteDLL(self, location):
        if self.head is None:
            return "empty singly list"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None

            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
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
                nextNode.next.prev = tempNode
                if tempNode.next is None:
                    self.tail = tempNode

    def deleteEntireDLL(self):
        if self.head is None:
            return "empty singly list"
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None


doublyLinkedList = DLinkedList()
doublyLinkedList.createDLL(1)
doublyLinkedList.insertDLL(3, -1)
doublyLinkedList.insertDLL(4, -1)
doublyLinkedList.insertDLL(0, 0)
doublyLinkedList.insertDLL(2, 2)
print([node.value for node in doublyLinkedList])
# doublyLinkedList.traverseDLL()
# print()
# doublyLinkedList.reverseTraverseDLL()
# print()
# print(doublyLinkedList.searchDLL(3))
# print(doublyLinkedList.searchDLL(5))
doublyLinkedList.deleteDLL(2)
print([node.value for node in doublyLinkedList])
doublyLinkedList.deleteEntireDLL()
print([node.value for node in doublyLinkedList])
