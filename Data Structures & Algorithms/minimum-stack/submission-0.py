class MinStack:

    def __init__(self):
        self.s = []
        self.smin = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.smin:
            self.smin.append(0)
        elif val < self.s[self.smin[-1]]:
            self.smin.append(len(self.s) - 1)

    def pop(self) -> None:
        if len(self.s) - 1 == self.smin[-1]:
            self.smin.pop()
        return self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.s[self.smin[-1]]
