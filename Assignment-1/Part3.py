#----------------------------------------------------------------------- STACK PART --------------------------------------------------------------------------------------------
class Stack():                                              
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) != 0:
            lastItem = self.stack[-1]
            self.stack.remove(lastItem)
            return lastItem
        else:
            return None
    def top(self):
        if len(self.stack) != 0:
            return(self.stack[-1])
        else:
            return None
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    def size(self):
        return len(self.stack)
    def min(self):
        if len(self.stack) != 0:
            return min(self.stack)
        else:
            return None
        
myStack = Stack()
myStack.push(42)
print("Top of stack: ", myStack.top())
print("Size of Stack: ", myStack.size())
popped_value = myStack.pop()
print("Popped value: ", popped_value)
print("Size of stack: ", myStack.size())
myStack.push(2)
myStack.push(3)
print("Minimum value: ", myStack.min())

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) != 0:
            lastItem = self.stack[-1]
            self.stack.remove(lastItem)
            return lastItem
        else:
            return None
    def top(self):
        if len(self.stack) != 0:
            return(self.stack[-1])
        else:
            return None
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    def size(self):
        return len(self.stack)
    def min(self):
        if len(self.stack) != 0:
            return min(self.stack)
        else:
            return None

myStack = Stack()
myStack.push(42)
print("Top of stack: ", myStack.top())
print("Size of Stack: ", myStack.size())
popped_value = myStack.pop()
print("Popped value: ", popped_value)
print("Size of stack: ", myStack.size())
myStack.push(2)
myStack.push(3)
print("Minimum value: ", myStack.min())

#----------------------------------------------------------------------- QUEUE PART --------------------------------------------------------------------------------------------
class Queue():                                              
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) > 0:
            frontItem = self.queue[0]
            self.queue.remove(frontItem)
            return frontItem
        else:
            return None
    def rear(self):
        if len(self.queue) > 0:
            return self.queue[-1]
        else:
            return None
    def front(self):
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return None
    def size(self):
        return len(self.queue)
    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

myQueue = Queue()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
print("Size of queue: ", myQueue.size())
print("Front of queue: ", myQueue.front())
print("Rear of queue: ", myQueue.rear())
dequeuedItem = myQueue.dequeue()
print("Dequeued Item: ", dequeuedItem)
