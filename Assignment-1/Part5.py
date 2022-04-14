'''
    def reverseIteratively(self, head: Node):
        prevNode = None
        currNode = self.head
        while currNode:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        return prevNode
'''
