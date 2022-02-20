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


# print("levelOrderTraversal")
# levelOrderTraversal(newBT)


# Search
def searchBT(rootNode, nodeValue):
    if not rootNode:
        return "Not found"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Found!"
            if (root.value.leftChild) is not None:
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild) is not None:
                customQueue.enqueue(root.value.rightChild)
        return "Not found"


# print("searchBT")
# print(searchBT(newBT, "N99"))


# Insert
def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.leftChild) is None:
                root.value.leftChild = newNode
                return "Inserted"
            else:
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild) is None:
                root.value.rightChild = newNode
                return "Inserted"
            else:
                customQueue.enqueue(root.value.rightChild)


# print("insertNodeBT")
# newNode = TreeNode("N8")
# print(insertNodeBT(newBT, newNode))
# levelOrderTraversal(newBT)


# Delete
def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild:
                customQueue.enqueue(root.value.leftChild)

            if root.value.rightChild:
                customQueue.enqueue(root.value.rightChild)
        return root.value


def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return

            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)

            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)


def deleteNodeBT(rootNode, nodeData):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeData:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "Deleted"

            if root.value.leftChild:
                customQueue.enqueue(root.value.leftChild)

            if root.value.rightChild:
                customQueue.enqueue(root.value.rightChild)

        return "Fail"


# print(deleteNodeBT(newBT, "N7"))
# levelOrderTraversal(newBT)


# Delete Tree
def deleteBT(rootNode):
    if not rootNode:
        return
    else:
        rootNode.data = None
        rootNode.leftChild = None
        rootNode.rightChild = None
        return "Deleted"


print(deleteBT(newBT))
levelOrderTraversal(newBT)
