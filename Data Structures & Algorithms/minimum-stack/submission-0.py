class MinStack:

    def __init__(self):
        self.st1 = list()
        self.st2 = list()

    def push(self, val: int) -> None:
        self.st1.append(val)
        if len(self.st2) == 0:
            self.st2.append(val)
        else:
            mini = min(self.st2[-1], val)
            self.st2.append(mini)

    def pop(self) -> None:
        self.st1.pop()
        self.st2.pop()

    def top(self) -> int:
        return self.st1[-1]

    def getMin(self) -> int:
        return self.st2[-1]
