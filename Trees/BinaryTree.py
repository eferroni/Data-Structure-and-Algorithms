import QueueLinkedList as queue

"""
    n1
    /\
 n2    n3
 /\    /\
n4 n5 n6 n7
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


newBT = TreeNode("N1")
n2Child = TreeNode("N2")
n4Child = TreeNode("N4")
n5Child = TreeNode("N5")
n2Child.leftChild = n4Child
n2Child.rightChild = n5Child

n3Child = TreeNode("N3")
n6Child = TreeNode("N6")
n7Child = TreeNode("N7")
n3Child.leftChild = n6Child
n3Child.rightChild = n7Child

newBT.leftChild = n2Child
newBT.rightChild = n3Child


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


# print("preOrderTraversal")
# preOrderTraversal(newBT)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


# print("inOrderTraversal")
# inOrderTraversal(newBT)


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    inOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


# print("postOrderTraversal")
# postOrderTraversal(newBT)


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild) is not None:
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild) is not None:
                customQueue.enqueue(root.value.rightChild)


print("levelOrderTraversal")
levelOrderTraversal(newBT)
