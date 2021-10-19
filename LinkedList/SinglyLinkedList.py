class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSSL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode

    def traverseSLL(self):
        if self.head is None:
            print("not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def searchSLL(self, value):
        if self.head is None:
            return "not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == value:
                    return "founded"
                node = node.next
            return "not found"

    def deleteSLL(self, location):
        if self.head is None:
            return "empty singly list"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
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
                    tempNode.next = None
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

    def deleteEntireSLL(self):
        if self.head is None:
            return "empty singly list"
        else:
            self.head = None
            self.tail = None


# singlyLinkedList = SLinkedList()
# node1 = Node(1)
# node2 = Node(2)

# singlyLinkedList.head = node1
# singlyLinkedList.head.next = node2
# singlyLinkedList.tail = node2

singlyLinkedList = SLinkedList()
singlyLinkedList.insertSSL(1, -1)
singlyLinkedList.insertSSL(2, -1)
singlyLinkedList.insertSSL(3, -1)
singlyLinkedList.insertSSL(4, -1)
singlyLinkedList.insertSSL(0, 0)
singlyLinkedList.insertSSL(0, 3)
print([node.value for node in singlyLinkedList])

# singlyLinkedList.traverseSLL()
# print(singlyLinkedList.searchSLL(4))
singlyLinkedList.deleteSLL(6)
print([node.value for node in singlyLinkedList])
print(singlyLinkedList.tail.value)
