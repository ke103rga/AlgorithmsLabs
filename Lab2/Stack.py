import numpy as np


class Stack:
    def __init__(self):
        self.data = []
        self.size = 0

    def push(self, elem):
        self.data.append(elem)
        self.size += 1

    def is_empty(self):
        return self.size == 0

    def pop(self):
        if not self.is_empty():
            self.size -= 1
            return self.data.pop()
        else:
            raise IndexError("The stack is empty")

    def __str__(self):
        stack_values = []
        while not self.is_empty():
            stack_values.append(self.pop())
        stack_values = stack_values[::-1]

        for value in stack_values:
            self.push(value)

        return stack_values.__str__()


def push_mean_value(mode="self_made", n=5):
    stack = Stack()
    if mode == "self_made":
        numbers_for_filling = [2, 4, 6, 8]
    else:
        numbers_for_filling = np.random.random(n)
    for number in numbers_for_filling:
        stack.push(number)

    print("The stack after pushing all numbers:")
    print(stack, end="\n\n")

    stack_values = []

    while not stack.is_empty():
        stack_values.append(stack.pop())
    mean_value = sum(stack_values) / len(stack_values)

    for value in stack_values[::-1]:
        stack.push(value)
    stack.push(mean_value)

    print(f"Mean value of all numbers: {mean_value}")

    print("Stack after pushing a mean value:")
    print(stack)


push_mean_value(mode="random")
