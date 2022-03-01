class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfString = False


class Trie:
    def __init__(self) -> None:
        self.rootNode = TrieNode()

    def insertString(self, word):
        current = self.rootNode
        for letter in word:
            ch = letter
            node = current.children.get(ch)
            if node is None:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.endOfString = True
        print("Inserted")

    def searchString(self, word):
        current = self.rootNode
        for letter in word:
            node = current.children.get(letter)
            if node is None:
                return False
            current = node
        if current.endOfString == False:
            return False
        else:
            return True


def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    canDelete = False

    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index + 1)
        return False

    if index == len(word) - 1:
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True

    if currentNode.endOfString == True:
        deleteString(currentNode, word, index + 1)
        return False

    canDelete = deleteString(currentNode, word, index + 1)
    if canDelete == True:
        root.children.pop(ch)
        return True
    else:
        return False


newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")

print(newTrie.searchString("App"))
print(newTrie.searchString("Appl"))
print(newTrie.searchString("Apple"))
print(newTrie.searchString("Ap"))

deleteString(newTrie.rootNode, "App", 0)

print(newTrie.searchString("App"))
print(newTrie.searchString("Appl"))
