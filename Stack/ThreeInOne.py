class MultiStack:
    def __init__(self) -> None:
        self.list = [None] * 3
        self.start_1 = 0
        self.end_1 = 0
        self.start_2 = 1
        self.end_2 = 1
        self.start_3 = 2
        self.end_3 = 2

    def __str__(self):
        return str(
            [
                self.list[self.start_1 : self.end_1 + 1],
                self.list[self.start_2 : self.end_2 + 1],
                self.list[self.start_3 : self.end_3 + 1],
            ]
        )

    def top(self):
        return str(
            [
                self.list[self.end_1],
                self.list[self.end_2],
                self.list[self.end_3],
            ]
        )

    def add(self, stack, value):
        if stack == 1:
            if self.list[self.start_1] is None:
                self.list[self.start_1] = value
            else:
                self.end_1 += 1
                self.list.insert(self.end_1, value)

                self.start_2 += 1
                self.end_2 += 1
                self.start_3 += 1
                self.end_3 += 1
        elif stack == 2:
            if self.list[self.start_2] is None:
                self.list[self.start_2] = value
            else:
                self.end_2 += 1
                self.list.insert(self.end_2, value)

                self.start_3 += 1
                self.end_3 += 1
        else:
            if self.list[self.start_3] is None:
                self.list[self.start_3] = value
            else:
                self.end_3 += 1
                self.list.append(value)

    def remove(self, stack):
        if stack == 1:
            value = self.list[self.end_1]
            if self.end_1 == self.start_1:
                self.list[self.end_1] = None
            else:
                self.list.pop(self.end_1)
                self.end_1 -= 1
                self.start_2 -= 1
                self.end_2 -= 1
                self.start_3 -= 1
                self.end_3 -= 1
        elif stack == 2:
            value = self.list[self.end_2]
            if self.end_2 == self.start_2:
                self.list[self.end_2] = None
            else:
                self.list.pop(self.end_2)
                self.end_2 -= 1
                self.start_3 -= 1
                self.end_3 -= 1
        else:
            value = self.list[self.end_3]
            if self.end_3 == self.start_3:
                self.list[self.end_3] = None
            else:
                self.list.pop()
                self.end_3 -= 1

        return value


custStack = MultiStack()
custStack.add(1, 1)
custStack.add(2, 2)
custStack.add(3, 3)
print(custStack)
custStack.add(1, 30)
custStack.add(2, 20)
custStack.add(3, 10)
print(custStack)
print("top:", custStack.top())
custStack.remove(3)
custStack.remove(1)
print(custStack)
custStack.remove(2)
print(custStack)
custStack.remove(2)
print(custStack)
custStack.remove(2)
print(custStack)
