class Stack:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        return not self.list

    def push(self, value):
        self.list.append(value)

    def pop(self):
        if not self.isEmpty():
            return self.list.pop()
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.list[-1]
        else:
            return None

    def delete(self):
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return "\n".join(values)


stack_list = Stack()

stack_list.push(0)
stack_list.push(1)
stack_list.push(2)
stack_list.push(3)
stack_list.push(4)
print(stack_list)
print(stack_list.peek())
stack_list.pop()
stack_list.pop()
stack_list.pop()
stack_list.pop()
stack_list.pop()
print(stack_list)
print(stack_list.peek())
