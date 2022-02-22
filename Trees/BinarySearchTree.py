"""
    70
    /\
 50    90
 /\    /\
30 60 80 100
"""


class BSTNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insertNode(rootNode, nodeValue):
    if rootNode.data is None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "Inserted"


newBST = BSTNode(None)

print(insertNode(newBST, 70))
print(insertNode(newBST, 60))
print(insertNode(newBST, 50))
print(newBST.data)
print(newBST.leftChild.data)
print(newBST.leftChild.leftChild.data)
