class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.max_size = maxSize
        self.count = 0

    def push(self, x: int) -> None:
        if self.count < self.max_size:
            self.stack.append(x)
            self.count += 1

    def pop(self) -> int:
        if self.stack:
            el = self.stack.pop(self.count - 1)
            self.count -= 1
            return el
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        if k < self.count:
            for i in range(0, k):
                self.stack[i] += val
        else:
            for i in range(0, len(self.stack)):
                self.stack[i] += val



# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)