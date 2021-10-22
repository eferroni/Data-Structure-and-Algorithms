from LinkedList import LinkedList


def SumLists(linked_list1, linkedlist2):
    node = linked_list1.head
    string_value1 = ""
    while node:
        string_value1 = str(node.value) + string_value1
        node = node.next

    node = linkedlist2.head
    string_value2 = ""
    while node:
        string_value2 = str(node.value) + string_value2
        node = node.next

    print(string_value1)
    print(string_value2)
    print(int(string_value1) + int(string_value2))


customLL1 = LinkedList()
customLL1.generate(4, 0, 3)
customLL2 = LinkedList()
customLL2.generate(4, 0, 3)
print(customLL1)
print(customLL2)

SumLists(customLL1, customLL2)
