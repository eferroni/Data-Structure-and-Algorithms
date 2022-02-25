class Heap:
    def __init__(self, size) -> None:
        self.customList = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1


def peekOfHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]


def sizeOfHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapSize + 1):
            print(rootNode.customList[i])


def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = index // 2
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            rootNode.customList[index], rootNode.customList[parentIndex] = (
                rootNode.customList[parentIndex],
                rootNode.customList[index],
            )
        heapifyTreeInsert(rootNode, parentIndex, heapType)

    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            rootNode.customList[parentIndex], rootNode.customList[index] = (
                rootNode.customList[index],
                rootNode.customList[parentIndex],
            )
        heapifyTreeInsert(rootNode, parentIndex, heapType)


def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "Full"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "Inserted"


def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                rootNode.customList[index], rootNode.customList[leftIndex] = (
                    rootNode.customList[leftIndex],
                    rootNode.customList[index],
                )
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                rootNode.customList[index], rootNode.customList[leftIndex] = (
                    rootNode.customList[leftIndex],
                    rootNode.customList[index],
                )
            return
    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex

            if rootNode.customList[index] > rootNode.customList[swapChild]:
                rootNode.customList[index], rootNode.customList[swapChild] = (
                    rootNode.customList[swapChild],
                    rootNode.customList[index],
                )
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex

            if rootNode.customList[index] < rootNode.customList[swapChild]:
                rootNode.customList[index], rootNode.customList[swapChild] = (
                    rootNode.customList[swapChild],
                    rootNode.customList[index],
                )
        heapifyTreeExtract(rootNode, swapChild, heapType)


def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0:
        return
    else:
        extractNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractNode


def deleteEntireBP(rootNode):
    rootNode.customList = None


newHeap = Heap(6)
print(insertNode(newHeap, 4, "Max"))
print(insertNode(newHeap, 5, "Max"))
print(insertNode(newHeap, 2, "Max"))
print(insertNode(newHeap, 1, "Max"))
# print(insertNode(newHeap, 6, "Max"))
# print(insertNode(newHeap, 3, "Max"))

print("peekOfHeap")
print(peekOfHeap(newHeap))

print("sizeOfHeap")
print(sizeOfHeap(newHeap))

print("levelOrderTraversal")
levelOrderTraversal(newHeap)

print("extractNode")
extractNode(newHeap, "Max")

print("levelOrderTraversal")
levelOrderTraversal(newHeap)

print("deleteEntireBP")
deleteEntireBP(newHeap)

print("levelOrderTraversal")
levelOrderTraversal(newHeap)
