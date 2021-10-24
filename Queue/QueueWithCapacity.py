class CircularQueue:
    def __init__(self, length) -> None:
        self.list = [None] * length
        self.length = length
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.list]
        return " -> ".join(values)

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.length:
            return True
        return False

    def isEmpty(self):
        return self.top == -1

    def enqueue(self, value):
        if self.isFull():
            return "full"
        else:
            if self.top + 1 == self.length:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.list[self.top] = value

    def dequeue(self):
        if self.isEmpty():
            return "empty"
        else:
            first_element = self.list[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.length:
                self.start = 0
            else:
                self.start += 1
            self.list[start] = None
            return first_element

    def peek(self):
        if self.isEmpty():
            return "empty"
        return self.list[self.start]

    def delete(self):
        self.list = [None] * self.length
        self.top = -1
        self.start = -1


circular_queue_list = CircularQueue(4)
print(circular_queue_list)
print(circular_queue_list.isFull())
print(circular_queue_list.isEmpty())
circular_queue_list.enqueue(0)
circular_queue_list.enqueue(1)
circular_queue_list.enqueue(2)
circular_queue_list.enqueue(3)
circular_queue_list.enqueue(4)
print(circular_queue_list)
circular_queue_list.dequeue()
print(circular_queue_list)
print(circular_queue_list.peek())
circular_queue_list.dequeue()
print(circular_queue_list)
print(circular_queue_list.peek())
circular_queue_list.delete()
print(circular_queue_list)
