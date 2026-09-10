class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        ans = self.stack2.pop()

        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return ans

    def peek(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        ans = self.stack2[-1]

        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return ans

    def empty(self):
        return len(self.stack1) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()