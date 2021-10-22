from LinkedList import LinkedList


def Return_nth_to_last(linked_list, nth):
    node = linked_list.head
    while node:
        temp_node = node
        for i in range(nth):
            if temp_node is None:
                print("higher than the len")
                return
            temp_node = temp_node.next
        if temp_node is None:
            print(node.value)
            return
        node = node.next


customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)

Return_nth_to_last(customLL, 10)
