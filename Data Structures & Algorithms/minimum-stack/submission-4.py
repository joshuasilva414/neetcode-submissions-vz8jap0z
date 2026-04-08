class MinStack:

    def __init__(self):
        self.data = []
        self.minIdxStack = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.minIdxStack or val <= self.data[self.minIdxStack[-1]]:
            self.minIdxStack.append(len(self.data)-1)

    def pop(self) -> None:
        self.data.pop()
        if self.minIdxStack and self.minIdxStack[-1] > len(self.data)-1:
            self.minIdxStack.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.data[self.minIdxStack[-1]]