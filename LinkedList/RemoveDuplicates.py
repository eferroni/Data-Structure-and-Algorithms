from LinkedList import LinkedList


def RemoveDuplicates(linkedList):
    list_value = set()
    node = linkedList.head
    while node:
        linkedList.tail = node
        if node.next is None:
            break
        list_value.add(node.value)
        temp_value = node.next
        while temp_value.value in list_value:
            if temp_value.next is None:
                temp_value = None
                break
            temp_value = temp_value.next
        node.next = temp_value
        node = node.next

    print(linkedList)


customLL = LinkedList()
customLL.generate(4, 0, 3)
print(customLL)

RemoveDuplicates(customLL)
