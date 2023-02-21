class Queue:
    def __init__(self, max_size=100):
        self.data = []
        self.size = 0
        self.max_size = max_size

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size >= self.max_size

    def push(self, elem):
        if not self.is_full():
            self.size += 1
            self.data.append(elem)
        else:
            print("The queue is overflowed")
            # raise IndexError("The queue is overflowed")

    def pop(self):
        if not self.is_empty():
            self.size -= 1
            return self.data.pop(0)
        else:
            print("The queue is underflowed")
            # raise IndexError("The stack is underflowed")

    def __str__(self):
        queue_values = []
        while not self.is_empty():
            queue_values.append(self.pop())

        for value in queue_values:
            self.push(value)

        return queue_values.__str__()


def test_queues():
    numbers_for_filling = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    q = Queue()
    for num in numbers_for_filling:
        q.push(num)

    print("The queue after filling:")
    print(q)

    queue_values = []
    while not q.is_empty():
        queue_values.append(q.pop())

    for value in queue_values[:-2]:
        q.push(value)
    q.push(queue_values[-1])
    q.push(queue_values[-2])

    print("The queue after switching two last elements:")
    print(q)


test_queues()
