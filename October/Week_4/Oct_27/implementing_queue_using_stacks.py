class MyQueue:

    def __init__(self):
        self.mainStack = []

    def push(self, x):
        self.mainStack.append(x)

    def pop(self):
        tempStack = []
        for i in range(len(self.mainStack)):
            tempStack.append(self.mainStack.pop())

        front = tempStack.pop()

        for j in range(len(tempStack)):
            self.mainStack.append(tempStack.pop())

        return front

    def peek(self):
        tempStack = []
        for i in range(len(self.mainStack)):
            tempStack.append(self.mainStack.pop())

        peek = tempStack[-1]

        for j in range(len(tempStack)):
            self.mainStack.append(tempStack.pop())
        return peek

    def empty(self):
        if len(self.mainStack) == 0:
            return True
        else: return False