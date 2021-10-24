class Queue:
    def __init__(self) -> None:
        self.list = []

    def isEmpty(self):
        return not self.list

    def peek(self):
        if self.isEmpty():
            return "empty queue"
        return self.list[0]

    def enqueue(self, value):
        self.list.append(value)

    def dequeue(self):
        if self.isEmpty():
            return "empty queue"
        return self.list.pop(0)

    def delete(self):
        self.list = []

    def __str__(self):
        values = [str(x) for x in self.list]
        return " -> ".join(values)


queue_list = Queue()
queue_list.enqueue(0)
queue_list.enqueue(1)
queue_list.enqueue(2)
queue_list.enqueue(3)
queue_list.enqueue(4)
print(queue_list)
print(queue_list.isEmpty())
print(queue_list.peek())
queue_list.dequeue()
print(queue_list)
print(queue_list.isEmpty())
print(queue_list.peek())
queue_list.delete()
print(queue_list)
