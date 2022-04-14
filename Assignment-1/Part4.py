class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def push(self, data):
        newNode = Node(data)
        currNode = self.head
        while currNode.next != None:
            currNode = currNode.next
        currNode.next = newNode

    def pop(self):
        prevNode = self.head
        currNode = self.head.next
        while (currNode.next != None):
            prevNode = prevNode.next
            currNode = currNode.next
        prevNode.next = None
        return currNode

    def size(self):
        currNode = self.head
        nodes = 0
        while currNode.next != None:
            nodes += 1
            currNode = currNode.next
        return nodes

    def display(self):
        elems = []
        currNode = self.head
        while currNode.next != None:
            currNode = currNode.next
            elems.append(currNode.data)
        print(elems)

    def insert(self, index, node):
        if 0 < index < self.size:
            prevNode = self.head
            nextNode = prevNode.next
            for i in range(index-1):
                prevNode = prevNode.next
                nextNode = nextNode.next
            prevNode.next = node
            node.next = nextNode

    def remove(self, index):
        if index > self.size():
            print("Index Out of Range")
            return
        curr_index = 0
        currNode = self.head
        while True:
            lastNode = currNode
            currNode = currNode.next
            if curr_index == index:
                lastNode.next = currNode.next
                return
            curr_index += 1

    def elementAt(self, index):
        if index >= self.size():
            print("Out of Range")
            return None
        current_index = 0
        currNode = self.head
        while True:
            currNode = currNode.next
            if current_index == index:
                return currNode.data
            current_index += 1

    def printList(self):
        linkedliststr = ""
        currNode = self.head
        while currNode.next != None:
            currNode = currNode.next
            linkedliststr += str(currNode.data) + " -> "

        print(linkedliststr)


lList = LinkedList()

#testPushBackAddsOneNode
lList.push(150)
lList.printList()

#testPopBackRemovesCorrectNode
lList.pop()
lList.printList()


for i in range(5):
    lList.push(i)


#testEraseRemovesCorrectNode
lList.remove(4)
lList.remove(0)
lList.printList()

#testEraseDoesNothingIfNoNode
lList.remove(0)
lList.remove(1)
lList.remove(3)
lList.printList()

#testElementAtReturnNode
elemnAt = lList.elementAt(0)
print(elemnAt)

#testElementAtReturnsNoNodeIfIndexDoesNotExist
elemnAt = lList.elementAt(1)
print(elemnAt)

#testSizeReturnsCorrectSize
print(lList.size())

for i in range(15):
    lList.push(i)
lList.printList()
lList.reverseIteratively()
lList.printList()
