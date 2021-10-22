from LinkedList import LinkedList


def Partition(linked_list, x):
    node = linked_list.head
    linked_list.tail = linked_list.head

    while node:
        nextNode = node.next
        node.next = None
        if node.value < x:
            node.next = linked_list.head
            linked_list.head = node
        else:
            linked_list.tail.next = node
            linked_list.tail = node
        node = nextNode
    if linked_list.tail.next:
        linked_list.tail.next = None
    print(linked_list)


customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)

Partition(customLL, 45)
